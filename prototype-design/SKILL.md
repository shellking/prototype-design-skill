---
name: prototype-design
description: HTML 高保真原型、线框与可点击 demo 绘制。基于真实页面 recon、组件复用、阶段审阅闸完成原型及验收。适用于画原型、改原型、做页面、校准真实产品样式。
---

# Prototype Design — 原型绘制入口

入口只保留**全程约束**；细节按阶段读取 `references/`。**按需加载 ≠ 省略阶段或闸门**。

本 skill 自包含模板、脚手架、容器设计系统与容器 lint。路径均相对本 skill 目录。

## 资产与工作流

| 资产 | 路径 | 用法 |
|---|---|---|
| 容器设计系统 | [design-system/prototype-container-design-system.md](design-system/prototype-container-design-system.md) | 写高保真前必读 |
| Stage0 摸底模板 | [templates/recon.md](templates/recon.md) | 复制到工作包再填 |
| Stage1 结构模板 | [templates/structure.md](templates/structure.md) | 复制到工作包再填 |
| Stage2 澄清模板 | [templates/clarify.md](templates/clarify.md) | 复制到工作包再填 |
| 线框骨架 | [scaffolds/wireframe.html](scaffolds/wireframe.html) | 复制后改结构 |
| 高保真空帧 | [scaffolds/hi-fi-frame.html](scaffolds/hi-fi-frame.html) | 复制后填产品槽 |
| 阶段过闸表 | [checklists/stages.md](checklists/stages.md) | **默认交付执行面** |
| 容器 lint | [scripts/check_container.py](scripts/check_container.py) | 高保真交付前建议跑 |
| 产品壳接法 | [adapters/PRODUCT.md](adapters/PRODUCT.md) | 对齐真实产品时阅读 |

工作包目录建议：`demands/<ID>/`。铁律：**复制 templates/scaffolds 再填，禁止空手编章节或从零拼容器 DOM。**

```bash
# 高保真交付前（相对本 skill 目录）
python scripts/check_container.py --file <原型.html> --format markdown
```

## 阶段路由与读取范围

每轮先识别当前阶段及已有的**用户批准证据**；先读本入口，再读本阶段必要文件。

| 当前任务 | 本轮读取 | 产物与推进条件 |
|---|---|---|
| Stage 0 摸底 | [起步与 recon](references/01-intake.md)；复制 `templates/recon.md` | recon 清单齐全 |
| Stage 1 结构与低保真 | [阶段与人工停点](references/02-stages.md)；`templates/structure.md` + `scaffolds/wireframe.html` | 结构稿+线框；交用户确认 |
| Stage 2 澄清 | [阶段与人工停点](references/02-stages.md)；`templates/clarify.md` | 澄清文档齐全；交用户确认 |
| Stage 3a/3b 高保真 | [编译与复用](references/03-compile.md)；[验收](references/04-verification.md)；`scaffolds/hi-fi-frame.html` | 样张证明入口/对象/状态变化/返回；获批后铺开；跑容器 lint |
| 修改已有原型 | [迭代](references/05-iteration.md) | 先回流澄清，再改稿 |
| Stage 3.5/4 自检与评审 | [验收](references/04-verification.md)；[checklist](checklists/stages.md) | 自检 → 独立评审 → 交用户 |
| 收尾 | [输出与降级](references/07-closeout.md) | 阶段、证据、未决项、下一步 |

命令与检查：见 [06-commands](references/06-commands.md)。默认走 checklist；本包唯一内置脚本是容器 lint。

## 全程不变的边界

- **真实源头**：已批准 PRD / 澄清 / 真实页 recon / 组件真相 才是源。
- **写第一行高保真前必读**：容器设计系统全文；团队产品壳约定（见 `adapters/PRODUCT.md`）。正文点名「已读」。
- **三层结构（固定）**：`.proto-frame ⊃ .proto-layout(row) ⊃ [.proto-stage ⊃ 壳 ⊃ 产品内容] + .note-panel`。局部改动用中性 wrapper 的红虚线 + 连续编号；净新增整页/整窗不圈虚线。
- **真实页身份**：每帧声明既有页局部改 / 净新增 / 样张。真实壳 ≠ 内容已对齐。
- **样式与文案**：主按钮在左、取消在右；单区一个主按钮。
- **可见验证**：声称对齐真实时，宽高/字号/overflow/截图需证据。

## 阶段与人工审阅

```
Stage 0 recon → Stage 1 结构 → 【用户审结构】→ Stage 2 澄清 → 【用户审澄清】
→ Stage 3a 样张 → 【用户拍样张】→ Stage 3b 铺开 → Stage 3.5 自检 → Stage 4 独立评审 → 【用户终审】
```

- 每轮只推进当前获准阶段。
- 「用户已确认」等字段只能引用真实后续用户输入，AI 不得代填。
- 多帧样张选 1～3 代表帧：入口、对象、状态变化、去向/返回。

## 交付证据

结构通过 ≠ 视觉正确。高保真交用户前：过 [checklists/stages.md](checklists/stages.md) 对应项，并建议 `check_container.py` PASS。「用户接受」不是跳过检查的豁免。

## 每轮输出

列：本轮复用件、需规避问题、自验/lint 结果、截图对比（若声称对齐）、当前阶段、未决问题、默认决策、下一步。详见 [07-closeout](references/07-closeout.md)。
