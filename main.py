# -*- coding: utf-8 -*-

import csv
import urllib
import sys
from bs4 import BeautifulSoup
from house_info import houses
from pic import picture
import pic
reload(sys)
sys.setdefaultencoding("utf-8")



def get_city_dict():
    city_dict = {}
    with open("citys.csv", "r") as f:
        reader = csv.reader(f)
        for city in reader:
            city_dict[city[1]] = city[0]
    return city_dict

def get_district(url):
    district_dict = {}
    html = urllib.urlopen(url)
    bsobj = BeautifulSoup(html.read(), "html5lib", from_encoding="utf-8")
    roles = bsobj.find("div", {"data-role":"ershoufang"}).findChildren("a")
    for i in roles:
        url = i.get("href")
        district_dict[i.get_text()] = url
        #print type(i),'testtype'
    return district_dict

def run():
    city_dict = get_city_dict()
    for city in city_dict.keys():
        print city,
    print
    input_city = raw_input("请输入城市：")
    city_url = city_dict.get(input_city)
    if not city_url:
        print "输入错误"
        sys.exit()
    ershoufang_city_url = city_url + "ershoufang"
    district_dict = get_district(ershoufang_city_url)
    for district in district_dict.keys():
        print district,
    print
    input_district = raw_input("请输入地区：").decode("utf-8")
    district_url = district_dict.get(input_district)
    if not district_url:
        print "输入错误"
        sys.exit()
    house_info_url = city_url + district_url[1:]
    print(house_info_url)
    houses(house_info_url)
    print("success")
    picture()

if __name__ == "__main__":
    run()



