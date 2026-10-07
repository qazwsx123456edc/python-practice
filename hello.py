# -*- coding: utf-8 -*-
"""我的第一个 Python 程序。

运行方式（任选一种）：
1. 在 VS Code 里打开这个文件，点右上角的 ▶ 运行按钮
2. 在终端里执行：python hello.py
"""

import platform
import sys

print("=" * 40)
print("你好，Python！")
print("=" * 40)
print(f"Python 版本 : {sys.version.split()[0]}")
print(f"运行平台   : {platform.system()} {platform.machine()}")
print(f"解释器路径 : {sys.executable}")
print()

# 1) 变量与 f-string
name = "同学"
hours_per_day = 2.5
print(f"{name}，你每天投入 {hours_per_day} 小时，一年就是 {hours_per_day * 365:.0f} 小时。")

# 2) 循环
print("\n一年 12 个月的累计小时数：")
total = 0.0
for month in range(1, 13):
    total += hours_per_day * 30
    print(f"  第 {month:2d} 个月累计 {total:7.1f} 小时")

# 3) 列表与推导式
skills = ["Python", "C", "数据结构", "算法", "项目"]
print("\n这一年的路线图：")
for index, skill in enumerate(skills, start=1):
    print(f"  {index}. {skill}")

# 4) 字典
进度 = {"Python": "进行中", "C": "待开始", "数据结构": "待开始"}
print("\n当前状态：", 进度)

print("\n如果上面这些你都看懂了，说明环境完全就绪，可以开始第一课了。")
