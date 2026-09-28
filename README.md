# Prototype Design Skill

面向产品经理与各类 AI Agent 协作的高保真 HTML 原型绘制 Skill。  
不绑定某一家工具；**模板 + 脚手架 + 容器设计系统 + 容器 lint** 开箱可跑。

适用：Cursor、Claude Code、Codex、ZCode、OpenCode、WorkBuddy 等支持 Agent Skill（`SKILL.md`）的环境。

## 安装

将整个 `prototype-design/` 目录放到你所用 Agent 的 **skills 目录**（名称因工具而异，常见为 `skills/`、`.agents/skills/`、`.claude/skills/`、`.cursor/skills/` 等）。

原则：

1. 目录名保持 `prototype-design`
2. 内含 `SKILL.md`，且相对路径（`templates/`、`scaffolds/`、`scripts/` …）不要拆散
3. 按该 Agent 文档重启/刷新 skill 列表后，在对话中点名使用（例如：「按 prototype-design 画原型」）

也可直接在本仓库根目录打开项目，让 Agent 读取 `./prototype-design/`。

## 目录

```text
prototype-design/
  SKILL.md
  references/       # 分阶段细则
  design-system/    # 容器/标注视觉语言
  templates/        # recon / 结构 / 澄清
  scaffolds/        # 线框骨架、高保真空帧
  checklists/       # 默认过闸表
  scripts/          # check_docs.py、check_container.py
  examples/         # 一份走通的小需求
  adapters/         # 如何挂真实产品壳
```

## 用法（最短路径）

0. 先看 `prototype-design/examples/demo-copy-action/`（填好的 recon、结构、澄清、HTML）
1. 复制 `templates/recon.md` → 填完再画
2. 复制 `templates/structure.md` + `scaffolds/wireframe.html` → 交用户审结构
3. 复制 `templates/clarify.md` → 交用户审澄清
4. 复制 `scaffolds/hi-fi-frame.html` → 填产品内容与说明
5. 勾选 `checklists/stages.md`
6. 高保真交付前（在 skill 目录下）：

```bash
python scripts/check_docs.py --file recon.md --file structure.md --file clarify.md
python scripts/check_container.py --file path/to/原型.html --format markdown
```

对齐真实产品视觉时，阅读 `adapters/PRODUCT.md`。

改造说明见 [ADAPT.md](./ADAPT.md)。

## 许可

MIT — 见 [LICENSE](./LICENSE)。
