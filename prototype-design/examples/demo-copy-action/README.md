# 样例：列表增加复制（DEMO-001）

一条小需求走完四帧，用来看这个 skill 的标注方式，而不是只看一个弹层。

| 帧 | 展示的特性 |
|---|---|
| 01 列表 | 已有页面只圈改动；侧栏和「编辑」不圈 |
| 02 弹层默认 | 编号和右栏一一对应；主按钮在左 |
| 03 保存失败 | 另一种状态单独成帧，编号继续用数字 |
| 04 空列表 | 整页状态不拆虚线，说明只写在右栏 |

```bash
python scripts/check_docs.py --file examples/demo-copy-action/recon.md --file examples/demo-copy-action/structure.md --file examples/demo-copy-action/clarify.md
python scripts/check_container.py --file examples/demo-copy-action/prototype.html --format markdown
```

04 没有画面编号，容器检查会给出警告，这是预期：整页状态不必强行贴编号。

左栏现在是示意界面。换成你们自己的真实壳时，只替换 `.proto-stage` 里的内容，见 `adapters/PRODUCT.md`。
