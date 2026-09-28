# 样例：列表增加「复制」（DEMO-001）

对照着改，比从空白模板起步快。文件都已填完，并且能过本包两道检查。

```bash
python scripts/check_docs.py --file examples/demo-copy-action/recon.md --file examples/demo-copy-action/structure.md --file examples/demo-copy-action/clarify.md
python scripts/check_container.py --file examples/demo-copy-action/prototype.html --format markdown
```

| 文件 | 对应阶段 |
|---|---|
| recon.md | Stage 0 |
| structure.md | Stage 1（轻量，免线框） |
| clarify.md | Stage 2 |
| prototype.html | Stage 3，从 `scaffolds/hi-fi-frame.html` 改来 |

产品区只有界面文案（复制 / 保存）。交互说明在右栏。接你们自己的真实壳时，替换 `.proto-stage` 里的弹层，见 `adapters/PRODUCT.md`。
