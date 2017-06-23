# -*- coding: utf-8 -*-
import sys
import csv
from urllib import urlopen
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://www.lianjia.com'

if __name__ == "__main__":
    html = urlopen(url).read()
    bsobj = BeautifulSoup(html, "html5lib")
    data = bsobj.find_all("div", {"class":"city-enum fl"})
    city_list = []
    for i in data:
        city = i.children
        for j in city:
            city_list.append(j)

    print city_list

    with open("city.csv", "wb") as f:
        writ = csv.writer(f)
        writ.writerow(["url", "city"])
        for i in city_list:
            writ.writerow((i.get("href"), i.get_text()))

