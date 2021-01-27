#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 15:40
# @Author  : Chocolate
# @Site    : 
# @File    : 预处理图片.py
# @Software: PyCharm

#提取目录下所有图片,更改尺寸后保存到另一目录
from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=516,height=387):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
# for jpgfile in glob.glob("E:\\img\\*.jpg"):
#     convertjpg(jpgfile,"E:\\lianhua")
if __name__ == '__main__':
    # path_name = "D:/TourismData/旅游者层面/图片/photo2.0/*.jpg"
    # out_dir = "D:/TourismData/旅游者层面/图片/resize_photo"
    # path_name = "D:/TourismData/政府层面/photo/*.jpg"
    # out_dir = "D:/TourismData/政府层面/resize_photo"
    path_name = "D:/TourismData/政府层面/picture2.0/*.jpg"
    out_dir = "D:/TourismData/政府层面/resize_picture2.0"
    for jpgfile in glob.glob(path_name):
         convertjpg(jpgfile,out_dir)