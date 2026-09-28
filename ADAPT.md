# 改造成适合你们团队的版本

## 1. 安装

拷贝整个 `prototype-design/` 到你所用 Agent 的 skills 目录（Cursor / Claude Code / Codex / ZCode / OpenCode / WorkBuddy 等均可，路径以各工具文档为准）。保持目录完整，勿拆散相对引用。

## 2. 必改

| 位置 | 改什么 |
|---|---|
| `SKILL.md` 的 `description` | 你们产品/终端的触发描述 |
| `templates/recon.md` 产线枚举 | 换成你们的端名称 |
| `adapters/PRODUCT.md` | 写清壳与 CSS 实际路径 |
| `scripts/check_container.py` 默认前缀 | 或交付时用 `--extra-real-prefix` |

## 3. 标注色/栏宽

改 `design-system/` 与 `scaffolds/hi-fi-frame.html` 内联 CSS 时，**整团队统一一版**，不要按需求临时改。

## 4. 可选增强

本包默认靠 checklist + 容器 lint。需要结构/澄清字段机检、截图 diff 时，在团队工程里自建，不必塞进本 skill。
