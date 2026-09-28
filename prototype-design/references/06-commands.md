> 按入口阶段路由加载。

## 默认执行面：人工 checklist

高保真交用户前，按 [checklists/stages.md](../checklists/stages.md) 勾选当前 Stage。机器检查通过不等于用户已审。

## 内置命令

在本 skill 目录下执行。

```bash
python scripts/check_docs.py --file <recon.md> --file <结构稿.md> --file <澄清.md>
python scripts/check_container.py --file <原型.html> --format markdown
```

- **check_docs**：recon / 结构稿 / 澄清是否还留着模板占位和空的必填格。
- **check_container**：容器类、横向 flex、虚线、pin 与右栏配对、虚线不挂真实组件类、产品区不写「本期新增」一类说明。

组件类前缀可追加：`--extra-real-prefix "myui-"`。

exit `0` = PASS；非 0 = FAIL。用户只要方向草稿时须在回复里降级，不能当成终稿。

先看填好的样例：[examples/demo-copy-action](../examples/demo-copy-action/README.md)。

## 团队自行搭建

真实壳是否复用、和线上截图像不像、声明式编译、交付总闸。接法见 [adapters/PRODUCT.md](../adapters/PRODUCT.md)。
