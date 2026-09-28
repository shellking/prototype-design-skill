#!/usr/bin/env python3
"""Check filled recon / structure / clarify docs are not still blank templates."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Tuple


PLACEHOLDERS = ("《需求ID》", "〔需求ID〕", "〔需求名〕", "〔页面/入口〕", "〔示例〕", "〔对象〕")


def issues_for(kind: str, text: str) -> List[str]:
    out: List[str] = []
    for mark in PLACEHOLDERS:
        if mark in text:
            out.append(f"仍含模板占位 {mark}")

    if kind == "structure":
        cell = _table_cell(text, "判定结论")
        if cell is None or not cell or cell in {"全套 / 轻量 / 跳过", "全套/轻量/跳过"}:
            out.append("§0 判定结论未填成「全套」「轻量」或「跳过」之一")
        if "L0 " not in text or "〔" in _section(text, "## §1"):
            # tree still template if section contains 〔
            pass
        sec1 = _section(text, "## §1 ")
        if "〔" in sec1:
            out.append("§1 页面树仍是模板括号，未改成实际页面")

    if kind == "clarify":
        row = _row_cells(text, "T-01")
        if row is None or len(row) < 3 or not row[2].strip():
            out.append("§3 文案表 T-01 文案为空")
        if "点击" not in text and "N/A" not in text:
            out.append("§1 缺少页面跳转（动作或 N/A）")

    if kind == "recon":
        cell = _table_cell(text, "productLine")
        if cell is None or not cell or "…" in cell or "..." in cell:
            out.append("productLine 未填具体产线")

    return out


def _section(text: str, heading_prefix: str) -> str:
    lines = text.splitlines()
    buf: List[str] = []
    on = False
    for line in lines:
        if line.startswith(heading_prefix):
            on = True
            continue
        if on and line.startswith("## "):
            break
        if on:
            buf.append(line)
    return "\n".join(buf)


def _table_cell(text: str, label: str) -> Optional[str]:
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0] == label and len(cells) >= 2:
            return cells[1]
    return None


def _row_cells(text: str, first: str) -> Optional[List[str]]:
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells and cells[0] == first:
            return cells
    return None


def detect_kind(path: Path) -> Optional[str]:
    name = path.name.lower()
    if "recon" in name:
        return "recon"
    if "clarif" in name or "澄清" in path.name:
        return "clarify"
    if "struct" in name or "结构" in path.name:
        return "structure"
    text = path.read_text(encoding="utf-8")
    if "productLine" in text and "styleSheets" in text:
        return "recon"
    if "微决策" in text:
        return "clarify"
    if "触发判定" in text:
        return "structure"
    return None


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Lint filled prototype docs against blank-template leftovers")
    ap.add_argument("--file", action="append", required=True, help="recon/structure/clarify markdown (repeatable)")
    ap.add_argument("--format", choices=("markdown", "text"), default="markdown")
    args = ap.parse_args(argv)

    rows: List[Tuple[str, str, str]] = []
    for raw in args.file:
        path = Path(raw)
        if not path.is_file():
            rows.append((str(path), "ERROR", "文件不存在"))
            continue
        kind = detect_kind(path)
        if not kind:
            rows.append((str(path), "ERROR", "无法识别文档类型（recon / 结构 / 澄清）"))
            continue
        text = path.read_text(encoding="utf-8")
        found = issues_for(kind, text)
        if not found:
            rows.append((str(path), "PASS", kind))
        else:
            for item in found:
                rows.append((str(path), "ERROR", f"{kind}: {item}"))

    errors = [r for r in rows if r[1] == "ERROR"]
    status = "PASS" if not errors else "FAIL"
    if args.format == "markdown":
        print(f"# doc lint: **{status}**")
        print()
        print("| 文件 | 结果 | 说明 |")
        print("|---|---|---|")
        for path, level, msg in rows:
            print(f"| `{path}` | {level} | {msg} |")
    else:
        for path, level, msg in rows:
            print(f"{level}\t{path}\t{msg}")
        print(status)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
