# 产品壳适配（像素对齐真实产品）

本 skill 开箱保证：**流程 + 容器标注规范**。  
对齐真实产品视觉，需要各团队自备壳与样式，按下面接进脚手架。

## 怎么接

1. 复制 `scaffolds/hi-fi-frame.html` 到工作包。
2. 删掉示范 `.demo-panel`（或整段替换）。
3. 在 `.proto-stage` 内放入：
   - 真实后台/移动壳 HTML 片段，或
   - 链入团队镜像 CSS + 壳 markup（注意 `file://` 下外链可能延迟加载）。
4. 局部改动用中性 `<span class="proto-dash">` 包住控件，pin 作子节点。
5. 跑：

```bash
python scripts/check_container.py --file <原型.html> --format markdown
```

若组件类前缀不在默认列表（`fa-` / `fu-` / `ant-` / `el-` …），追加：

```bash
python scripts/check_container.py --file <html> --extra-real-prefix "myui-"
```

## 建议团队私有维护

| 资产 | 说明 |
|---|---|
| 真实壳 HTML | PC / 移动完整壳 |
| CSS / 字体镜像 | 按真实加载序 |
| 组件 snippet INDEX | 可复用片段 |
| 反模式库 | 产线踩坑 |

这些放在**私有仓库**，不要写回本开源 skill。

## 本 skill 不负责

- 登录真实环境、拉取业务数据
- 自动编译器 / 像素 diff 流水线（可按同目标自建）
