#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 有关帧图片的一些参数
# 宽 80个单位
# 高 30个单位
# 帧率 ：30/sec

import Image
import os
import time

# 如同之前公开课讲授的，将文件路径指向的图片文件转换成字符画
# 保存在`pic_str`中返回
# 阈值为128，大于阈值的用' '表示白色，小于的用‘#’表示黑色
def ImageAscii(filepath):
    img = Image.open(filepath)
    img = img.convert('L')
    pix = img.load()
    width , height = img.size
    pic_str = ''
    for h in xrange(height):
        for w in xrange(width):
            if (int(pix[w,h]) < 128):
                pic_str += '#'
            else:
                pic_str += ' '
        pic_str += '\n'
    return pic_str

# 针对`filelist`的排序函数
# 对于`bdXXXXXX`的文件名形式根据后六位数字从小到大依次排序
def file_cmp(x,y):
    a = int(x.split('.')[0][2:])
    b = int(y.split('.')[0][2:])
    if a == b:
        return 0
    if a > b:
        return 1
    else:
        return -1

# 设置文件类型和帧图片所在路径
filetype = 'bmp'
capturefolder = "/home/grzhan/Windows_G:/Capture/"

# 帧图片的宽高
width = 80
height = 30

# os.listdir 有点相当于Linux命令行下的`ls`命令，
# 获取指定目录下的文件，并以 list 的形式返回
filelist = os.listdir(capturefolder)
pic_string = ''
filelist.sort(cmp=file_cmp)

for file_ in filelist:
    if file_.split('.')[1] == filetype:
        img_str = ImageAscii(capturefolder + file_)
        # sleep是一个延时函数，用来控制播放速度
        # 为音画同步提供基础，这里的含义就是延迟0.051秒
        time.sleep(0.051)
        # 在Linux Shell使用的清屏函数
        # 在Windows下请使用 os.system("cls")
        os.system("clear")
        print img_str
        pic_string += img_str
