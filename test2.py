# -*- coding: utf-8 -*-
# filename: citys.py

import csv
from urllib import urlopen
from bs4 import BeautifulSoup

url = "https://www.lianjia.com"

html = urlopen(url).read()
# 获取 BeautifulSoup 对象，用 html5lib 解析（也可用 lxml 或其它方式解析，html5lib 容错性较好，所以此处选用 html5lib ）
bsobj = BeautifulSoup(html, "html5lib")

citys_tag = bsobj.find("div", {"class":"fc-main clear"}).findChildren("a")
for city_tag in citys_tag:
    print city_tag
