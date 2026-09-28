#!/usr/bin/env python3
"""Container-layer lint for prototype HTML (stdlib only)."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional, Tuple


DEFAULT_REAL_PREFIXES = ("fa-", "fu-", "fuview-", "ant-", "el-", "van-", "mui-", "arco-")


@dataclass
class Issue:
    level: str
    code: str
    message: str


@dataclass
class Frame:
    label: str
    depth: int
    canvas_pins: List[str] = field(default_factory=list)
    note_pins: List[str] = field(default_factory=list)
    has_layout: bool = False
    has_stage: bool = False
    has_note: bool = False
    dash_on_real: List[List[str]] = field(default_factory=list)


class PrototypeParser(HTMLParser):
    def __init__(self, real_prefixes: Tuple[str, ...]) -> None:
        super().__init__(convert_charrefs=True)
        self.real_prefixes = real_prefixes
        self.styles: List[str] = []
        self.frames: List[Frame] = []
        self._open_frames: List[Frame] = []
        self._depth = 0
        self._in_style = False
        self._style_buf: List[str] = []
        self._capture_pin = False
        self._pin_buf: List[str] = []
        self._pin_kind: Optional[str] = None
        self._in_note_panel_depth: Optional[int] = None

    def _is_real_class(self, cls: str) -> bool:
        if cls.startswith(("proto-", "note-", "doc-", "band", "demo-", "legend", "product-")):
            return False
        return any(cls.startswith(p) for p in self.real_prefixes)

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        self._depth += 1
        ad = {k: (v or "") for k, v in attrs}
        classes = set((ad.get("class") or "").split())

        if tag == "style":
            self._in_style = True
            self._style_buf = []
            return

        if "proto-frame" in classes:
            frame = Frame(
                label=ad.get("data-screen-label") or f"frame#{len(self.frames) + 1}",
                depth=self._depth,
            )
            self.frames.append(frame)
            self._open_frames.append(frame)

        frame = self._open_frames[-1] if self._open_frames else None
        if frame is None:
            return

        if "proto-layout" in classes:
            frame.has_layout = True
        if "proto-stage" in classes:
            frame.has_stage = True
        if "note-panel" in classes:
            frame.has_note = True
            self._in_note_panel_depth = self._depth

        if "proto-dash" in classes:
            bad = sorted(c for c in classes if self._is_real_class(c))
            if bad:
                frame.dash_on_real.append(bad)

        if "proto-pin" in classes:
            in_note = (
                self._in_note_panel_depth is not None
                and self._depth >= self._in_note_panel_depth
            )
            is_corner = "proto-pin-tl" in classes or "proto-pin-tr" in classes
            self._capture_pin = True
            self._pin_buf = []
            if is_corner and not in_note:
                self._pin_kind = "canvas"
            else:
                self._pin_kind = "note"

    def handle_endtag(self, tag: str) -> None:
        if tag == "style" and self._in_style:
            self._in_style = False
            self.styles.append("".join(self._style_buf))
            self._style_buf = []
            self._depth = max(0, self._depth - 1)
            return

        if self._capture_pin:
            text = "".join(self._pin_buf).strip()
            frame = self._open_frames[-1] if self._open_frames else None
            if frame is not None and text and self._pin_kind:
                if self._pin_kind == "canvas":
                    frame.canvas_pins.append(text)
                else:
                    frame.note_pins.append(text)
            self._capture_pin = False
            self._pin_kind = None
            self._pin_buf = []

        if self._open_frames and self._open_frames[-1].depth == self._depth:
            self._open_frames.pop()

        if self._in_note_panel_depth is not None and self._depth == self._in_note_panel_depth:
            self._in_note_panel_depth = None

        self._depth = max(0, self._depth - 1)

    def handle_data(self, data: str) -> None:
        if self._in_style:
            self._style_buf.append(data)
        if self._capture_pin:
            self._pin_buf.append(data)

    def handle_startendtag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        # void tags: count depth briefly
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)


def _extract_rule(css: str, selector_pat: str) -> List[str]:
    return [
        m.group(0)
        for m in re.finditer(selector_pat + r"\s*\{([^{}]*)\}", css, flags=re.I | re.S)
    ]


def check_css(css: str, issues: List[Issue]) -> None:
    if "#f5222d" not in css.lower():
        issues.append(Issue("WARN", "PROTO_C_COLOR", "未发现标注红 #f5222d"))

    after = _extract_rule(css, r"\.proto-dash::after")
    base = _extract_rule(css, r"\.proto-dash(?![:\w-])")
    dash_text = "\n".join(after + base)
    if ".proto-dash" in css:
        if after:
            if "dashed" not in "\n".join(after):
                issues.append(
                    Issue("ERROR", "PROTO_C_DASH_BORDER", "proto-dash::after 须含 dashed border")
                )
        elif "dashed" not in dash_text:
            issues.append(
                Issue("ERROR", "PROTO_C_DASH_BORDER", "proto-dash 须使用 dashed border / ::after")
            )
        if re.search(r"outline\s*:", dash_text) and "border" not in dash_text:
            issues.append(
                Issue("ERROR", "PROTO_C_OUTLINE", "proto-dash 不得只靠 outline")
            )

    layout_rules = _extract_rule(css, r"\.proto-layout")
    layout_text = "\n".join(layout_rules)
    if not layout_rules:
        issues.append(Issue("ERROR", "PROTO_C_LAYOUT_CSS_MISSING", "缺少 .proto-layout CSS 规则"))
    else:
        if not re.search(r"display\s*:\s*flex", layout_text):
            issues.append(Issue("ERROR", "PROTO_C_LAYOUT_NOT_FLEX", ".proto-layout 必须 display:flex"))
        if re.search(r"flex-direction\s*:\s*column", layout_text):
            issues.append(
                Issue(
                    "ERROR",
                    "PROTO_C_LAYOUT_COLUMN",
                    ".proto-layout 禁止 flex-direction:column（说明栏会掉到下方）",
                )
            )


def analyze(html: str, real_prefixes: Tuple[str, ...]) -> List[Issue]:
    issues: List[Issue] = []
    parser = PrototypeParser(real_prefixes)
    try:
        parser.feed(html)
        parser.close()
    except Exception as exc:  # noqa: BLE001
        return [Issue("ERROR", "PROTO_C_PARSE", f"HTML 解析失败: {exc}")]

    css = "\n".join(parser.styles)
    if not css.strip():
        issues.append(Issue("ERROR", "PROTO_C_NO_STYLE", "未找到 <style>；容器 CSS 须同文件嵌入"))
    else:
        check_css(css, issues)

    for cls in ("proto-frame", "proto-layout", "proto-stage", "note-panel"):
        if not re.search(rf'class=["\'][^"\']*\b{re.escape(cls)}\b', html):
            issues.append(Issue("ERROR", "PROTO_C_STRUCT", f"文档缺少 .{cls}"))

    if not parser.frames:
        issues.append(Issue("ERROR", "PROTO_C_STRUCT", "未发现 .proto-frame"))
        return issues

    for frame in parser.frames:
        label = frame.label
        if not frame.has_layout:
            issues.append(Issue("ERROR", "PROTO_C_STRUCT", f"帧「{label}」缺少 .proto-layout"))
        if not frame.has_stage:
            issues.append(Issue("ERROR", "PROTO_C_STRUCT", f"帧「{label}」缺少 .proto-stage"))
        if not frame.has_note:
            issues.append(Issue("ERROR", "PROTO_C_STRUCT", f"帧「{label}」缺少 .note-panel"))

        for bad in frame.dash_on_real:
            issues.append(
                Issue(
                    "ERROR",
                    "PROTO_C_DASH_ON_REAL",
                    f"帧「{label}」: proto-dash 与真实组件类同挂一元素 {bad}；须用中性 wrapper",
                )
            )

        canvas = frame.canvas_pins
        notes = frame.note_pins
        if len(canvas) != len(set(canvas)):
            issues.append(Issue("ERROR", "PROTO_C_PIN_DUP", f"帧「{label}」画面 pin 重复: {canvas}"))
        for num in canvas:
            if num not in notes:
                issues.append(
                    Issue(
                        "ERROR",
                        "PROTO_C_PIN_NOTE_MISSING",
                        f"帧「{label}」画面编号 {num} 在右栏无对应",
                    )
                )
        for num in notes:
            if num not in canvas:
                issues.append(
                    Issue(
                        "ERROR",
                        "PROTO_C_NOTE_PIN_MISSING",
                        f"帧「{label}」右栏编号 {num} 在画面无对应 pin",
                    )
                )
        if not canvas and not notes:
            issues.append(
                Issue(
                    "WARN",
                    "PROTO_C_NO_PIN",
                    f"帧「{label}」无 pin（净新增整页可不圈；局部改动应有编号）",
                )
            )

    return issues


def format_markdown(issues: List[Issue], path: Path) -> str:
    errors = [i for i in issues if i.level == "ERROR"]
    warns = [i for i in issues if i.level == "WARN"]
    status = "PASS" if not errors else "FAIL"
    lines = [
        f"# container lint: **{status}**",
        f"- file: `{path}`",
        f"- errors: {len(errors)}",
        f"- warnings: {len(warns)}",
        "",
    ]
    if not issues:
        lines.append("无问题。")
        return "\n".join(lines)
    lines.append("| 级别 | 代码 | 说明 |")
    lines.append("|---|---|---|")
    for i in issues:
        lines.append(f"| {i.level} | `{i.code}` | {i.message} |")
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Lint prototype container/annotation layer")
    ap.add_argument("--file", required=True, help="prototype HTML path")
    ap.add_argument("--format", choices=("markdown", "text"), default="markdown")
    ap.add_argument(
        "--extra-real-prefix",
        action="append",
        default=[],
        help="extra class prefix treated as real components (repeatable)",
    )
    args = ap.parse_args(argv)

    path = Path(args.file)
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    html = path.read_text(encoding="utf-8")
    prefixes = tuple(DEFAULT_REAL_PREFIXES) + tuple(args.extra_real_prefix or [])
    issues = analyze(html, prefixes)

    if args.format == "markdown":
        print(format_markdown(issues, path))
    else:
        for i in issues:
            print(f"{i.level}\t{i.code}\t{i.message}")
        print("PASS" if not any(i.level == "ERROR" for i in issues) else "FAIL")

    return 1 if any(i.level == "ERROR" for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
