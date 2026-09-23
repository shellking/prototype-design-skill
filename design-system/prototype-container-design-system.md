---
title: 原型容器设计系统（原型本身的设计系统 · 左右布局）
scope: 所有产品线原型的「外壳/容器」——版式 + 标注视觉语言 + 说明结构 + 文档元信息
核心立场: 原型本身也是产品（用户=研发/测试/产品评审），必须有固定设计系统；布局/虚线/编号/配色不得一个需求一个样
---

# 原型容器设计系统

> **两类设计系统别混淆**：
> - **产品设计系统** = 被临摹的真实产品（壳、组件、Token）。
> - **本文件 = 原型文档自己的外壳**：画板怎么摆、虚线/编号/说明长什么样。
>
> **两条铁律**：
> 1. 版式/标注/配色**全部固定**，AI 无权逐需求发挥（「这次左右下次上下」「这次红下次紫」一律禁止）。
> 2. **产品层 = 真实壳，绝不臆造**：有真实效果就用真实效果——这是「保证效果」的唯一手段。

---

## 0. 标准 = 两层，来源不同

| 层 | 谁定 | 来源 |
|---|---|---|
| ① 容器/标注系统（左右布局、红虚线、编号、说明面板、图例、文档头） | **authored（本文件）** | 本设计系统 |
| ② 产品层（后台壳/小程序壳/业务组件） | **绝不 author，只复用真实** | 真实产品 CSS + 真实壳片段 |

---

## A. 画布与版式（左右布局）

### A1 帧结构（固定）

```
.proto-frame（白卡）
 ├─ .proto-frame-head（帧标题 + 帧号）
 └─ .proto-layout（flex 行）
     ├─ .proto-stage（产品左，flex:1，overflow-x:auto——产品在栏内横滚，壳不动）
     └─ .note-panel（说明右，固定 300px，常驻）
```

### A2 平台 profile（每端固定）

| 平台 | 产品（左栏 .proto-stage 内） | 说明（右栏） |
|---|---|---|
| **PC 管理后台** | **真实后台壳全宽**，宽则栏内横滚 | 300px 常驻 |
| **移动端** | **真实手机/小程序壳**（如 phone 375 / wrap 399），多状态横向并排 | 300px 常驻 |

关键：PC 不缩小（真实多宽就多宽，靠 `.proto-stage{overflow-x:auto}` 栏内横滚，说明栏始终可见）。

### A3 出血/间距/栅格

- 帧白卡 + `.proto-stage` padding 24；帧间距 ≥14；间距走 4 倍数。
- 多帧纵向堆叠，每帧自身左右布局。

### A4 编号/标签

- 每帧带 `data-screen-label="01 标题"`（1-indexed，供评审定位 + 设计工具拆 frame）。

---

## B. 标注视觉系统（红 #f5222d，高区分度）

### B1 三层模型

① 产品 UI 层（真实壳，只真实文案）｜② 标注层（红虚线/红编号/右栏说明）｜③ 过程层（复刻/沟通，只进 recon/对话）。

### B2 虚线 `.proto-dash`（`::after` 浮层，**不挤动产品**）

- `position:relative` + `::after{ position:absolute; left:-5px;right:-5px;top:-4px;bottom:-4px; border:1px dashed #f5222d; border-radius:3px; pointer-events:none; z-index:6; }`
- **关键**：用 `::after` 浮层，不用 border-in-box——产品要被量像素，标注一推就失真。
- **铁律**：`proto-dash` **绝不直接加在真实产品元素上**（真实组件常带 `overflow` 裁剪，`::after` 画在框外会被裁掉）。正确做法：用 authored 的中性 wrapper 包住要圈的控件，编号 pin 作为该 wrapper 的子节点。

```html
<!-- ✗ 错误：proto-dash 挂真实组件，::after 被 overflow 裁掉 -->
<div class="real-row real-form-item proto-dash">
  <span class="proto-pin proto-pin-tl">1</span>
  …真实控件…
</div>

<!-- ✓ 正确：author 的 wrapper 包住要圈的控件 -->
<div class="real-row real-form-item">…label…
  <span class="proto-dash" style="display:inline-block;position:relative">
    <span class="proto-pin proto-pin-tl">1</span>
    <div class="real-control-group">…真实控件…</div>
  </span>
</div>
```

- 语义边界：虚线用于区分「本期变化」与「本期不变」。只在既有页面/既有弹窗上圈真实变化的局部元素，禁粗暴圈整行/整卡/整弹窗。**整页或整窗净新增不圈虚线**，说明放右侧 note-panel。note-panel 只写交互说明/业务规则，禁写「为什么只圈/虚线怎么用」这类规范话术。

### B3 编号 `.proto-pin`（贴框角外侧，**不进内容流**）

- 18×18 红圆、白字 `600 12px`；`.proto-pin-tr`（右上角外侧）、`.proto-pin-tl`（左上角）。
- 说明正文内联用同款（`.note-item .proto-pin`）。
- **编号规则**：同需求内连续；主改动用**数字** 1,2,3…，独立状态帧用**字母** A,B…；画面 pin 与右栏说明同号**一一对应**。

### B4 标注红 vs 产品危险红

标注红 `#f5222d` 永远以「虚线圈 + 编号圆 + 右栏说明」形态出现；产品危险红是产品按钮/文字。靠形态与层次区分。

---

## C. 说明内容结构

### C1 说明面板 `.note-panel`

- `width:300px; border-left:1px solid #eef0f3; background:#fff; padding:16px 18px`。
- 标题 `.note-panel-title`：红 `#f5222d` 600 14px + 底部 `1px dashed #ffccc7` 分隔。
- 每条 `.note-item`：`display:flex; gap:8px; font-size:13px; line-height:1.75`。
- **白底不用橙块**：产品是主角，标注克制退后。

### C2 每条说明字段

`编号 + 类型标签 + 正文`。类型 `.note-typ`：交互 / 状态 / 规则 / 边界 / 版本门控。

### C3 说明多时分组

按帧/类型分块；一个控件多态 → 并排多帧（字母编号）或说明内逐态列。

---

## D. 文档元信息

- **文档头 `.doc-head`**：需求名 ｜ ID ｜ 版本 ｜ 产线 ｜ 终端 ｜ 状态 ｜ 日期。
- **图例 legend**：`红虚线=本期变化点`｜`红编号=对应右侧说明`。
- 区块标题带 `.band`（蓝竖条 + 文字）分 PC / 移动等大段。

---

## E. 覆盖度约定

- 状态清单：空 / 加载 / 错误 / 置灰 / 极值 —— 必画或说明声明。
- 每可点元素有去向；帧间跳转标注关系。

---

## F. 导出兼容

- 设计工具捕获：svg `<use>` 尽量 inline；虚线用 border/`::after` 非 outline；说明 `min-width:0` 防溢出。
- 自包含：捕获类建议内联关键 CSS（双击零 FOUC）。命名建议 `<ID>-原型-<帧>-v<n>.html`。

---

## G. 固定 CSS（左右版，所有原型 include，禁逐需求改值）

```css
/* === 原型容器设计系统 —— 标注红 #f5222d === */
.doc-head{ background:#fff; border-bottom:1px solid #e3e6ea; padding:13px 24px; display:flex; align-items:center; gap:14px; flex-wrap:wrap; position:sticky; top:0; z-index:100; }
.band{ padding:22px 24px 2px; font-size:15px; font-weight:600; display:flex; align-items:center; gap:8px; }
.band::before{ content:""; width:4px; height:15px; background:#3370FF; border-radius:2px; }
.proto-frame{ margin:14px 24px 0; background:#fff; border-radius:6px; box-shadow:0 1px 4px rgba(0,0,0,.08); }
.proto-frame-head{ display:flex; justify-content:space-between; align-items:center; padding:13px 18px; border-bottom:1px solid #eef0f3; background:#fbfbfc; }
.proto-layout{ display:flex; align-items:stretch; }
.proto-stage{ flex:1; min-width:0; position:relative; overflow-x:auto; overflow-y:visible; background:#eef1f5; padding:24px; }
.note-panel{ width:300px; flex-shrink:0; border-left:1px solid #eef0f3; background:#fff; padding:16px 18px; }
.note-panel-title{ color:#f5222d; font-weight:600; font-size:14px; margin:0 0 14px; padding-bottom:10px; border-bottom:1px dashed #ffccc7; }
.note-item{ display:flex; gap:8px; margin-bottom:16px; font-size:13px; line-height:1.75; color:rgba(0,0,0,.72); }
.note-item b{ color:#333; }
.note-typ{ display:inline-block; font-size:11px; color:#d4380d; border:1px solid #ffccc7; border-radius:3px; padding:0 5px; margin-right:5px; line-height:17px; }
.proto-dash{ position:relative; }
.proto-dash::after{ content:""; position:absolute; left:-5px; right:-5px; top:-4px; bottom:-4px; border:1px dashed #f5222d; border-radius:3px; pointer-events:none; z-index:6; }
.proto-pin{ display:inline-flex; width:18px; height:18px; border-radius:50%; background:#f5222d; color:#fff; font:600 12px/1 sans-serif; align-items:center; justify-content:center; flex-shrink:0; }
.proto-pin-tr{ position:absolute; top:-9px; right:-9px; z-index:7; }
.proto-pin-tl{ position:absolute; top:-9px; left:-9px; z-index:7; }
.note-item .proto-pin{ margin-top:1px; }
```

## Enforcement

- 原型必须 include 上述 CSS，且**产品层为真实壳**。
- 建议机检：class 存在 + 固定值未改 + 虚线为 border/`::after` 非 outline + 每个画面 pin 落在 authored 的 `proto-dash` wrapper 内（wrapper 不得带真实产品组件类名）+ 画面 pin ↔ 说明编号配对。
