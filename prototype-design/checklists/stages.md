# 阶段过闸表（默认执行面）

每过一闸：勾选产物、粘贴**用户原话**（AI 不得代填）。未勾完不得声称可审阅。

## Stage 0 · recon

- [ ] 已复制并填写 `templates/recon.md`
- [ ] 产线 / 形态 / 样式表 / 目标组件有证据
- [ ] 正文列出可复用与需规避

## Stage 1 · 结构

- [ ] 已复制 `templates/structure.md`
- [ ] 全套时已复制并改 `scaffolds/wireframe.html`
- [ ] `check_docs.py` 对结构稿 PASS
- [ ] **用户已确认结构**：______

## Stage 2 · 澄清

- [ ] 已复制 `templates/clarify.md`
- [ ] `check_docs.py` 对澄清 PASS
- [ ] 页面流 mermaid 或 N/A+理由
- [ ] **用户已确认澄清**：______

## Stage 3a · 样张

- [ ] 基于 `scaffolds/hi-fi-frame.html`
- [ ] 1～3 代表帧覆盖入口/对象/状态变化/返回
- [ ] `python scripts/check_container.py --file <样张.html> --format markdown` → PASS（或已降级声明）
- [ ] **用户已拍样张**：______

## Stage 3b · 铺开

- [ ] 其余帧与澄清一致
- [ ] 容器 lint PASS

## Stage 3.5 / 4 · 自检与评审

- [ ] 逐态 / 文案净化 / 无重叠溢出 已自检
- [ ] 独立第二人（或第二模型）已过
- [ ] **用户终审**：______
