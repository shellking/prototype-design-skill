# DEMO-001 开局摸底 recon（Stage 0）

> 这是填好的样例，对照 `templates/recon.md`。需求：列表操作列增加「复制」。

| 字段 | 内容 | 证据 |
|---|---|---|
| 需求 ID / 名称 | DEMO-001 / 列表增加复制 | PRD §1 |
| productLine | admin | 管理后台列表页 |
| styleSheets | app.css, components.css（按页面实际 link 顺序） | 浏览器样式表清单 |
| viewportWidth | 1440 | 实测 |
| rootScale | 1 | 无外层缩放 |
| runtimeKind | spa | 前端路由页 |
| targetComponent | list-page | 列表根节点 |
| targetRect | 1200×640 | 内容区实测 |
| pageForm | 独立页 | 列表为独立路由 |
| reusableSnippets | 现有列表壳；操作列为按钮组 | 线上列表页 |
| truthCards | 降级：本样例无源码卡 | — |
| antiPatterns | 不要在产品区写「本期新增」；复制不要新开整页 | — |

## 结论

- [x] 清单齐全，可进 Stage 1
- [ ] 阻塞项：无
