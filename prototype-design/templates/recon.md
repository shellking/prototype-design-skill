# 《需求ID》开局摸底 recon（Stage 0）

> 复制本文件到 `demands/<ID>/<ID>-recon.md` 再填。未填完禁止写高保真 HTML。

| 字段 | 内容 | 证据 |
|---|---|---|
| 需求 ID / 名称 | | |
| productLine | admin / mobile / … | |
| styleSheets | 真实加载序 CSS 清单（禁止猜路径） | |
| viewportWidth | | |
| rootScale | （iframe 外层 scale；无则 1） | |
| runtimeKind | static / spa / uni-app / 其它 | |
| targetComponent | 顶层类名 | |
| targetRect | 实测宽×高 | |
| pageForm | 独立页 / 模块嵌入 / 弹窗 / 侧栏 / 子视图 | |
| reusableSnippets | 可复用壳/组件 + 硬性约束 | |
| truthCards | 源码真相覆盖（有源码必填；无则写「降级：无源码」） | |
| antiPatterns | 本轮需规避 | |

## 结论

- [ ] 清单齐全，可进 Stage 1
- [ ] 阻塞项：______
