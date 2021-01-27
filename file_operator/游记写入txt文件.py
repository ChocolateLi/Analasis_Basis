#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 14:18
# @Author  : Chocolate
# @Site    : 
# @File    : 游记写入txt文件.py
# @Software: PyCharm

# 读取excel表格的数据并写进txt文件

import pandas as pd
import os

# def creatcatesdir(data, target):
#     """
#     创建类别目录
#     """
#     # 获取去重后的分类列表
#     cates = list(data['relative breeds'].unique())
#     print(cates)
#     for cate in cates:
#         # 拼接子目录路径
#         final_path = target + cate
#         try:
#             os.mkdir(final_path)  # 创建目录
#         except Exception as e:
#             print(str(e))


def excel2txt(data, target):
    # 创建类别目录
    # creatcatesdir(data, target)

    # 逐条获取excel中的内容
    for index, row in data.iterrows():

        try:
            # 文件名 -> 文章标题
            filename = row['title']
            # 标题链接
            title_url = row['title_url']
            # 文件内容 -> 正文
            content = row['note']
            # unicode中的‘\xa0’字符在转换成gbk编码时会出现问题，gbk无法转换'\xa0'字符。
            # 所以，在转换的时候必需进行一些前置动作
            # 将'\xa0‘替换成u' '空格
            content = content.replace(u'\xa0', u'')
            # 去除多余的空格和空行
            content = content.replace('\n', '').replace('\r', '').replace(' ','')
            # 拼接文件路径
            txt_path = target
            # 将文章内容写入txt
            with open(txt_path + str(filename) + ".txt", 'wt',encoding='utf-8') as f:
                f.write(filename + '\n' + title_url + '\n'+ content)
            print("第"+str(index+1)+"篇文章写入完成")
        except Exception:
            print(Exception)



def main():
    # 使用pandas读取excel
    data = pd.read_excel('D:/TourismData/旅游者层面/数据3.0/未统计的游记.xlsx')
    # 主目录 需要提前创建好
    targetfile = "D:/TourismData/旅游者层面/数据3.0/未统计的article/"
    excel2txt(data, targetfile)


if __name__ == '__main__':
    print("Processing...")
    main()
    print("Succeed...")