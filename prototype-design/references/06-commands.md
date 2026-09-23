> 按入口阶段路由加载。下列是检查清单；团队可按同等目的接入自动化工具。

## 建议检查面

| 能力 | 用途 | 何时跑 |
|---|---|---|
| coverage diff | PRD 期望 vs 结构稿/澄清覆盖 | 每个 gate 前 |
| structure lint | 结构确认稿必填段 | Stage 1 |
| clarify lint | 澄清文档必填段与来源 | Stage 2 |
| container lint | 左右布局、虚线不挂真实组件、pin↔说明配对 | 高保真后 |
| annotation lint | 产品 UI 层禁混入交互说明/「新增」徽标 | 高保真后 |
| shell reuse lint | 禁手画假壳、禁隐藏标准壳 | 整页帧 |
| sample gate | 样张 HTML sha + 截图绑定 | Stage 3a |
| pre-emit selfcheck | 运动员交卷前自检 | Stage 3.5 |
| delivery gate | 终稿证据齐全 | 交用户前 |
| visual diff | real vs local / 上版 vs 本版 | 声称对齐时 |
| render truth audit | 「节点在但没画出来」空白/0 高 | 真实壳交付前 |
| frame digest | 全量 vs 增量通道判定 | 迭代交付 |
| registry lock | 壳/组件漂移拒编 | 每次编译 |
| audit completeness | 空跑哨兵（工作集为空假绿） | 每份审计产物 |

## 手动最小集

无自动化时至少保证：

1. Stage 停点有用户原话批准记录
2. 容器 CSS 来自设计系统且未改色值/栏宽
3. 虚线包在中性 wrapper 上，pin 与右栏同号
4. 声称对齐真实时：并排截图 + 关键尺寸表 + overflow 检查
5. 独立第二人/第二模型过一眼再交需求方
