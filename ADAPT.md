# 如何改造成适合你们团队的 Skill

本仓库是**可 fork 的起点**，不是某家公司的完整产线。按下面顺序改，通常最快。

## 1. 复制到本机 Skill 目录

Cursor 项目级（推荐，跟仓库一起走）：

```text
.cursor/skills/prototype-design/
```

或个人级：

```text
~/.cursor/skills/prototype-design/
```

把本仓库的 `prototype-design/` 整目录拷过去即可。其它 Agent（Claude Code / Codex 等）按各自 skill 目录约定放置。

## 2. 必改三处

| 位置 | 改什么 |
|---|---|
| `SKILL.md` frontmatter `description` | 改成你们产品/终端的触发描述 |
| `references/01-intake.md` | 换成你们的产线名、真实页 recon 方式、组件库入口 |
| `design-system/` | 若标注色/栏宽要改，**整团队统一改一版**，禁止按需求临时改 |

## 3. 建议接上的本地能力（可选）

原完整产线依赖自动化闸（lint / 编译 / 截图对比）。开源包**不附带**这些脚本与平台数据。你们可以：

1. 先用人审闸跑通 Stage 0→4（本 skill 已写清停点）
2. 再按 `references/06-commands.md` 的**概念清单**自研或接入等价脚本
3. 把真实产品壳 / 组件库放在**私有仓库**，不要回写到本开源包

## 4. 不要做的事

- 不要把内部密码、业务数据、个人使用记录提交回本仓库或公开 fork
- 不要把产品设计系统（真实壳、业务 Token）混进本 skill；本仓库只收**容器/标注**设计系统
- 不要把无关 skill（Figma、文案、规划等）塞进同一目录

## 5. 贡献回上游

欢迎 PR：**通用方法论改进**、容器 CSS 缺陷修复、文档澄清。含内网路径或业务数据的改动会被拒绝。
