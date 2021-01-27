#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 15:21
# @Author  : Chocolate
# @Site    : 
# @File    : 重命名图片.py
# @Software: PyCharm

import os

#path_name='D:/TourismData/旅游者层面/图片/photo2.0'
#path_name='D:/TourismData/旅游者层面/图片/到到网'
#path_name='D:/TourismData/政府层面/photo'
path_name='D:/TourismData/政府层面/picture2.0'


#path_name :表示你需要批量改的文件夹
i=1
for item in os.listdir(path_name):#进入到文件夹内，对每个文件进行循环遍历
    # print(item)
    os.rename(os.path.join(path_name,item),os.path.join(path_name,(str(i)+'.jpg')))#os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
    i+=1
print("重命名完成")
