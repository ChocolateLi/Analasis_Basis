#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/3 12:06
# @Author  : Chocolate
# @Site    : 
# @File    : 爬虫网页链接图片.py
# @Software: PyCharm

import pandas as pd

def main():
    file = ""
    readURL(file)

# 读取excel文件的某一列数据（网页链接url）
def readURL(file):
    table = pd.read_excel(file)
    clo = table['页面网址']
    print(clo)


if __name__ == '__main__':
    main()