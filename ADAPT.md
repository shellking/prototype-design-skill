# 改造成适合你们团队的版本

## 1. 放到本机 Skill 目录

Cursor 项目级（推荐）：

```text
.cursor/skills/prototype-design/
```

或个人级：

```text
~/.cursor/skills/prototype-design/
```

把本仓库的 `prototype-design/` 整目录拷过去即可。其它 Agent 按各自 skill 目录约定放置。

## 2. 按团队改三处

| 位置 | 改什么 |
|---|---|
| `SKILL.md` 的 `description` | 改成你们产品/终端的触发描述 |
| `references/01-intake.md` | 换成你们的产线名、真实页 recon 方式、组件库入口 |
| `design-system/` | 标注色/栏宽若要改，整团队统一改一版，不要按需求临时改 |

## 3. 可选：接上自动化

本 skill 写清了阶段停点与检查项。有工程能力的团队可按 `references/06-commands.md` 接入 lint / 截图对比等工具；没有也可以先用人审闸跑通全流程。

## 4. 贡献

欢迎 PR：方法论改进、容器 CSS 缺陷修复、文档澄清。
