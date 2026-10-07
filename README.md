# python-practice · 练习目录使用说明

这个文件夹就是你接下来一年的**代码练习场**。目录约定：

```
python-practice/
├── hello.py            环境自检脚本（能不能跑通看它）
├── week1/              第 1 周的练习和作业
│   ├── temp_converter.py   作业 1：温度转换器
│   └── seconds.py          作业 2：秒数换算
├── week2/              第 2 周（自己新建文件夹）
└── ...
```

> **文件命名用英文**（`temp_converter.py` 而不是 `温度转换器.py`）。原因：以后 `import`、Git、命令行都会用到文件名，中文名容易踩坑。**中文写在注释和输出里完全没问题。**

---

## 三种运行方式

### 方式 1：VS Code 里点按钮（最省事）
打开某个 `.py` 文件 → 点右上角的 ▶ 三角形 → 输出显示在下方的终端里。

### 方式 2：终端里敲命令（推荐，最接近真实开发）
在 VS Code 里按 `Ctrl + ~` 打开终端，然后：

```powershell
cd week1
python temp_converter.py
```

### 方式 3：REPL 交互模式（试语法最快）
终端里直接输入 `python`，出现 `>>>` 后就可以一行一行试：

```
>>> 2 + 3
5
>>> "abc".upper()
'ABC'
>>> exit()
```

---

## 用 Git 保存进度

仓库已经建好并推到 GitHub 了：<https://github.com/qazwsx123456edc/python-practice>
（远端已关联为 `origin`，分支是 `main`）

**每天收尾就三行：**

```powershell
cd D:\dsh.workspace\python-practice
git add .
git commit -m "feat: 完成温度转换器"
git push
```

第一次 push 已经让你在浏览器里授权过一次了，之后不用再登录。

### 提交信息怎么写（现在养成习惯）

| 前缀 | 什么时候用 | 例子 |
| --- | --- | --- |
| `feat` | 新增功能 / 完成一份练习 | `feat: 完成秒数换算` |
| `fix` | 修好一个 bug | `fix: 修正除零报错` |
| `docs` | 只改文档或注释 | `docs: 补充运行说明` |
| `chore` | 杂项（整理、配置） | `chore: 添加 .gitignore` |

### 随时查看状态

```powershell
git status            # 哪些改动还没提交
git log --oneline     # 提交历史
git diff              # 具体改了哪几行
```

---

## 常见问题

| 现象 | 解决 |
| --- | --- |
| 终端里 `python` 不是内部或外部命令 | 关掉终端重新开一个（PATH 是新写的）；或在 VS Code 里 `Ctrl+Shift+P` → `Python: Select Interpreter` → 选 `3.14.8` |
| 中文打印成乱码 | 终端里执行 `chcp 65001` |
| ▶ 按钮点了没反应/选了错解释器 | `Ctrl+Shift+P` → `Python: Select Interpreter` → 选 `C:\Users\123\AppData\Local\Programs\Python\Python314\python.exe` |
| 报错 `SyntaxError` | 看报错最后一行的**行号**，通常是缩进、冒号、括号写错 |
| 提示 `ModuleNotFoundError` | 缺第三方库，用 `pip install 库名` 装（标准库不用装） |

**每天的固定收尾动作：跑一遍今天的代码 → `git add . && git commit`。**
