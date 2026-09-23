# Prototype Design Skill（开源）

面向产品经理与 Agent 协作的**高保真 HTML 原型绘制** Skill：阶段流水、人工审阅闸、容器标注设计系统。

同事可直接使用，也可 fork 后改成适合自己产线的版本（见 [ADAPT.md](./ADAPT.md)）。

## 本仓库包含什么

```text
prototype-design/          # 唯一 Skill
  SKILL.md                 # 入口与全程约束
  references/              # 分阶段细则（按需加载）
design-system/
  prototype-container-design-system.md   # 原型外壳/标注视觉语言（唯一附带设计系统）
```

## 本仓库刻意不包含

- 其它无关 Skill（如 Figma 同步、规划、文案等）
- 真实产品设计系统、真实壳 HTML、组件 snippet、CSS 镜像
- 密码、凭据、内网地址、业务需求数据、个人使用记录
- 某家公司的平台 Runtime / Hook / 自动化脚本实现

## 快速开始

1. 将 `prototype-design/` 拷到 Cursor 的 `.cursor/skills/prototype-design/`（或个人 `~/.cursor/skills/`）
2. 将 `design-system/prototype-container-design-system.md` 放到你们仓库固定路径，并在 `SKILL.md` 里改引用路径
3. 在对话中明确使用本 skill（例如：「按 prototype-design 画原型」）
4. 按 Stage 0→1→2→3→4 推进；**每个 Stage 之间必须停等人工审阅**

## 核心原则（摘要）

1. **先 recon 再画**：真实页面/组件摸底未过，禁止写第一行高保真 HTML
2. **产物 ≠ 过闸**：结构稿 / 澄清 / 样张 / 终稿都要用户真审；AI 不得自填「用户已确认」
3. **容器固定**：左右布局、红虚线、编号、右栏说明——见容器设计系统，禁止按需求改配色/版式
4. **产品层复用真实**：有真实壳/组件就复用；禁止手画近似壳冒充对齐
5. **可见验证**：声称对齐真实时，要有宽高/字号/overflow/截图对比证据，不能只靠口头

## 许可

MIT — 见 [LICENSE](./LICENSE)。
