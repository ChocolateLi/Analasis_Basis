#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 19:59
# @Author  : Chocolate
# @Site    : 
# @File    : DownloadPhoto.py
# @Software: PyCharm

# pandas读取excel表格链接
# 通过requests库进行下载图片

import pandas as pd
import requests

path = "D:/TourismData/weixin"

def readExcel(file):
    excelfile = pd.read_excel(file)
    urls = excelfile['url']
    return urls


def downloadPhoto(urls):
    for i in range(len(urls)):
        r = requests.request('get', urls[i])  # 获取网页
        print(r.status_code)
        if(r.status_code==200):
            with open(path  + str(i) + '.jpg', 'wb') as f:  # 打开写入到path路径里-二进制文件，返回的句柄名为f
                f.write(r.content)  # 往f里写入r对象的二进制文件
            f.close()


if __name__ == '__main__':
    file = "D:/weixin_photo.xlsx"
    urls = readExcel(file)
    downloadPhoto(urls)