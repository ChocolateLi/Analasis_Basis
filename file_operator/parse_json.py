#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 10:49
# @Author  : Chocolate
# @Site    : 
# @File    : parse_json.py
# @Software: PyCharm

# python解析json，并把json数据写入excel

import os
import json
import xlwt

def get_json_info(path_name):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象，相当于一个文件
    sheet = book.add_sheet('图片分析', cell_overwrite_ok=True)  # 创建工作表
    col = ("关键字", "概率")
    row = 1
    for i in range(0,2):
        # 第0行，第i列
        sheet.write(0,i,col[i]) # 列名
    all_json = os.listdir(path_name)
    for json_name in all_json:
        # print(path_name + json_name)
        json_txt = open(path_name + json_name)
        json_info = json.load(json_txt)
        images = json_info['images'][0] # type:dict
        bi_concepts = images['bi-concepts'] # type:dict
        for i,(k,v) in enumerate(bi_concepts.items()):
            sheet.write(row,0,k)
            sheet.write(row,1,v)
            row += 1
            # 只取前五个关键字
            if(i==4):
                break
    book.save(r"D:/parse_json.xls")
if __name__ == '__main__':
    # path_name = "D:/TourismData/政府层面/test_json/"
    # path_name = "D:/TourismData/政府层面/图片解析/"
    path_name = "D:/TourismData/旅游者层面/图片/图片解析/"
    get_json_info(path_name)
    print("succeed")