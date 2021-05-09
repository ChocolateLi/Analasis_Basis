#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/9 8:28
# @Author  : Chocolate
# @Site    : 
# @File    : move_json.py
# @Software: PyCharm

import shutil
import os

# 将一个文件夹下的json文件移动到另一个文件夹
def move_file(old_path,new_path):
    for file in os.listdir(old_path):
        if file.endswith('.json'):
            src = os.path.join(old_path,file)
            dst = os.path.join(new_path,file)
            shutil.move(src,dst)

# 删除以.dat结尾的文件
def remove_dat(old_path):
    for file in os.listdir(old_path):
        if file.endswith(".dat"):
            src = os.path.join(old_path, file)
            os.remove(src)


if __name__ == '__main__':
    old_path = 'D:/TourismData/resize_photo'
    new_path = 'D:/TourismData/json_file'
    # move_file(old_path,new_path)
    remove_dat(old_path)
    print("完成")