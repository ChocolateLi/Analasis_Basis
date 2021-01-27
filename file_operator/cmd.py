#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 20:09
# @Author  : Chocolate
# @Site    : 
# @File    : cmd.py
# @Software: PyCharm

# python调用window下cmd的命令

import os

print("测试开始")
cmd = "python sentiBank.py D:/test/test_image"
os.system(cmd)
print("测试结束")