#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 11:41
# @Author  : Chocolate
# @Site    : 
# @File    : test_excel.py
# @Software: PyCharm

# 测试创建excel表格
import xlwt

book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象，相当于一个文件
sheet = book.add_sheet('图片分析', cell_overwrite_ok=True)  # 创建工作表
col = ("关键字", "概率")
for i in range(0,2):
    sheet.write(0,i,col[i]) # 列名

for row in range(1,9):
    sheet.write(row,0,"test1")
    sheet.write(row,1,"test2")

book.save(r"D:/test_excel.xls")