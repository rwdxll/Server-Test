#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:wdl 
# time:2017-03-08 pm

import os
import sys
import time
import requests
from PIL import Image
import pytesseract
import subprocess

code_url = "http://www.jiuaixianzhi.com/yxshop/randCodeImage"
#code_url = "https://www.jiguang.cn/captcha/login/"

def identification_code(url):

	#获取验证码并保存
	with open("captcha.jpg","wb") as i:
		i.write(requests.get(url,stream=True).content)

	#打开图片
	im = Image.open("captcha.jpg")

	#转化图片为灰度图
	im = im.convert('L')

	def initTable(threshold=140):
		table = []
		for i in range(256):
			if i < threshold:
				table.append(0)
			else:
				table.append(1)
		return table

	#灰度图二值化
	bininaryImage = im.point(initTable(),'1')

	#将图片转化为文本
	return pytesseract.image_to_string(bininaryImage,lang="eng",config="-psm 7")

print(identification_code(code_url))