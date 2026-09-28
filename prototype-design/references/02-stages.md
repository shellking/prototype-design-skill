> 按入口阶段路由加载。

## 阶段流水

每个 **■** 是 end-turn 人工停止点。

```
Stage 0  recon（复制 templates/recon.md）
   ↓
Stage 1  结构稿 + 线框（templates/structure.md + scaffolds/wireframe.html）
   ↓ ■停：用户审结构
Stage 2  澄清（templates/clarify.md）
   ↓ ■停：用户审澄清
Stage 3a 样张（scaffolds/hi-fi-frame.html，1～3 代表帧）
   ↓ ■停：用户拍样张
Stage 3b 铺开其余帧
   ↓
Stage 3.5 自检 + 建议跑 check_container.py
   ↓
Stage 4  独立评审
   ↓ ■停：用户终审
Stage 5  收尾
```

**判定快捷**：纯复刻可轻量/跳过 Stage1（在结构稿 §0 写明）；新增模块 / 新形态 / 大改造 → 全套。

**产出契约**：每轮只推进一个 Stage，写明现处第几 Stage、下一步是产物还是等用户。

---

## 最高纪律：人工审阅闸

> **产物 ≠ 过闸。过闸 = 用户真的审过。**

1. 一轮只产一个 Stage 的产物，然后必须停。
2. 「用户已确认」禁止 AI 自填——只能引用后续轮次用户原话。
3. Stage 间是否继续由人工拍板。
4. 用户已接受 ≠ 改文件后可跳过重核。

### 澄清与批次

澄清应含页面跳转流；纯单页可写 N/A + 理由。多 Batch 时维护覆盖矩阵。
