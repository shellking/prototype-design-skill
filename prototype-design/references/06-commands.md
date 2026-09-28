> 按入口阶段路由加载。本包唯一内置可执行命令是容器 lint；其余用 checklist。

## 默认执行面：人工 checklist

高保真交用户前，按 [checklists/stages.md](../checklists/stages.md) 勾选当前 Stage。没有勾完不得声称可审阅。

## 内置命令：容器 lint

```bash
# 相对本 skill 目录
python scripts/check_container.py --file <原型.html> --format markdown
```

检查：容器类齐全、`.proto-layout` 横向 flex、标注红与虚线形态、pin↔说明配对、`proto-dash` 不挂真实组件类前缀。

可选扩展禁用前缀：

```bash
python scripts/check_container.py --file <html> --extra-real-prefix "myui-" --format markdown
```

exit `0` = PASS；非 0 = FAIL，禁止递交用户终审（除非用户明确只要方向草稿并已降级声明）。

## 团队可自建的检查（本包不附带）

若团队有工程能力，可自建：结构/澄清字段 lint、截图 diff、壳复用检查等。未自建时，用 checklist 与人工对照模板必填段即可。
