# -*- coding: utf-8 -*-
# filename: citys.py

import csv

from urllib import urlopen
from bs4 import BeautifulSoup

url = "https://www.lianjia.com"

# 获取 html 页面
html = urlopen(url).read()

# 获取 BeautifulSoup 对象，用 html5lib 解析（也可用 lxml 或其它方式解析，html5lib 容错性较好，所以此处选用 html5lib ）
bsobj = BeautifulSoup(html, "html5lib")

# 得到 class="fc-main clear" 的 div 下所有 a 标签
#city_tags = bsobj.find("div", {"class":"fc-main clear"}).findChildren("a")
city_tags = bsobj.find("div", {"class":"link-list"}).div.dd.findChildren("a")

"""
    city_tags 内数据的格式如下

    <a title="天津房产网" href="https://tj.lianjia.com/">天津</a>
    <a title="青岛房产网" href="https://qd.lianjia.com/">青岛</a>
    ...
"""

# 将每一条数据抽离，保存在 citys.csv 文件中
with open("./citys.csv", "w") as f:
    writ = csv.writer(f)
    for city_tag in city_tags:
        # 获取 <a> 标签的 href 链接
        city_url = city_tag.get("href").encode("utf-8")
        # 获取 <a> 标签的文字，如：天津
        city_name = city_tag.get_text().encode("utf-8")
        writ.writerow((city_name, city_url))
        print city_name, city_url
