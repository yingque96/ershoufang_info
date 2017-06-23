# -*- coding: utf-8 -*-

import re
import csv
import urllib
from bs4 import BeautifulSoup


# 成功打开页面时返回页面对象，否则为空
def get_bsobj(url):
    page = urllib.urlopen(url)
    if page.getcode() == 200:
        html = page.read()
        bsobj = BeautifulSoup(html, "html5lib")
        return bsobj
    else:
        return None

# 获取页面中所有的房屋详情页的 url
def get_house_url_list(url):
    house_url_list = []
    bsobj = get_bsobj(url)
    if not bsobj:
        return None
    house_tag_list = bsobj.find_all("li", {"class": "clear"})
    print house_tag_list
    if house_tag_list:
        house_url_list.extend([house.a.get("href") for house in house_tag_list])
    return house_url_list

def get_house_info_list(url):
    house_info_list = []
    bsobj = get_bsobj(url)
    if not bsobj:
        return None

    house_list = bsobj.find_all("li", {"class":"clear"})

    # 标题
    for house in house_list:
        title = house.find("div", {"class": "title"}).get_text()
        """
        # 价格
        price = bsobj.find("span", {"class": "total"}).get_text()
        # 面积大小
        size = bsobj.find("div", {"class": "area"}).div.get_text()
        # 小区
        block = bsobj.find("div", {"class": "communityName"}).a.get_text()
        # 房型
        house_type = bsobj.find("div", {"class": "room"}).div.get_text()
        """
        info = house.find("div", {"class": "houseInfo"}).get_text().split("|")
        # 小区
        block = info[0].strip()
        # 房型
        house_type = info[1].strip()
        size_info = info[2].strip()
        # 面积大小 保留整数
        size = re.findall(r"\d+", size_info)[0]
        price_info = house.find("div", {"class": "totalPrice"}).span.get_text()
        # 价格 保留整数
        price = re.findall(r"\d+", price_info)[0]
        house_info_list.append({
            "title": title,
            "price": int(price),
            "size": int(size),
            "block": block,
            "house_type": house_type
        })
    return house_info_list

def houses(url):
    house_info_list = []
    for i in range(3):
        new_url = url + 'pg' + str(i+1)

        house_info_list.extend(get_house_info_list(new_url))
    if house_info_list:
        with open("house.csv", "wb+") as f:
            writer = csv.writer(f, delimiter="|")
            for house_info in house_info_list:
                title = house_info.get("title")
                price = house_info.get("price")
                size = house_info.get("size")
                #size = re.findall(r"\d+", size_info)[0]
                block = house_info.get("block")
                house_type = house_info.get("house_type")
                writer.writerow([title, int(price), int(size), block, house_type])
                print block, price, size
