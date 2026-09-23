# Security & Desensitization

本仓库**只**发布可复用的原型绘制方法论与「原型容器设计系统」。贡献或 fork 时请遵守：

## 严禁提交

| 类别 | 示例 |
|---|---|
| 密码 / 凭据 | 账号密码、API Key、Token、Cookie、`.secrets/`、OAuth 配置 |
| 业务数据 | 真实用户/学员/订单/课程内容、内部 PRD 全文、需求工单原文 |
| 系统运维数据 | 内网 URL、环境配置、平台 Runtime 契约、Hook 注册表、个人使用记录 |
| 产品设计系统 | 真实产品壳 HTML、组件 snippet 库、业务设计 Token、CSS 镜像 |
| 无关 Skill | Figma 同步、规划、文案、考勤等其它 skill |

## 允许提交

- `prototype-design/` 下的 skill 入口与 references（方法论）
- `design-system/prototype-container-design-system.md`（原型外壳/标注视觉语言）
- README / ADAPT / LICENSE / 本文件

## 脱敏检查清单（发 PR 前）

- [ ] 全文无真实域名、内网地址、账号、密码、token
- [ ] 无具体业务需求 ID、工单正文、客户/学员数据
- [ ] 无个人工作台路径、使用日志、验收放行凭据
- [ ] 未附带其它 skill 或产品壳模板
