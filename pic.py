# -*- coding: utf-8 -*-
# filename: pic.py

import csv
import numpy
import matplotlib.pyplot as plt

# 读取 house.csv 文件中价格和面积列
price, size = numpy.loadtxt('house.csv', delimiter='|', usecols=(1, 2), unpack=True)

print price
print size

# 求价格和面积的平均值
price_mean = numpy.mean(price)
size_mean = numpy.mean(size)

print "平均价格为：", price_mean 
print "平均面积为：", size_mean

# 求价格和面积的方差
price_var = numpy.var(price)
size_var = numpy.var(size)

print "价格的方差为：", price_var
print "面积的方差为：", size_var

plt.figure()
plt.subplot(211)
#plt.title("price")
plt.title("/ 10000RMB")
plt.hist(price, bins=20)

plt.subplot(212)
#plt.title("area")
plt.xlabel("/ m**2")
plt.hist(size, bins=20)

plt.figure(2)
plt.title("price")
plt.plot(price)

plt.show()
