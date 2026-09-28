# Prototype Design Skill

面向产品经理与 Agent 协作的高保真 HTML 原型绘制 Skill。  
离开特定平台也能跑通：**模板 + 脚手架 + 容器设计系统 + 容器 lint**。

## 安装

将整个 `prototype-design/` 目录拷到：

```text
.cursor/skills/prototype-design/
```

或个人 `~/.cursor/skills/prototype-design/`。

## 目录

```text
prototype-design/
  SKILL.md
  references/       # 分阶段细则
  design-system/    # 容器/标注视觉语言
  templates/        # recon / 结构 / 澄清
  scaffolds/        # 线框骨架、高保真空帧
  checklists/       # 默认过闸表
  scripts/          # check_container.py
  adapters/         # 如何挂真实产品壳
```

## 用法（最短路径）

1. 复制 `templates/recon.md` → 填完再画
2. 复制 `templates/structure.md` + `scaffolds/wireframe.html` → 交用户审结构
3. 复制 `templates/clarify.md` → 交用户审澄清
4. 复制 `scaffolds/hi-fi-frame.html` → 填产品内容与说明
5. 勾选 `checklists/stages.md`
6. 高保真交付前：

```bash
cd .cursor/skills/prototype-design   # 或本仓库内路径
python scripts/check_container.py --file path/to/原型.html --format markdown
```

对齐真实产品视觉时，阅读 `adapters/PRODUCT.md`。

改造说明见 [ADAPT.md](./ADAPT.md)。

## 许可

MIT — 见 [LICENSE](./LICENSE)。
