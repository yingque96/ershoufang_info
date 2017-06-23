# -*- coding: utf-8 -*-


import csv
import numpy
import matplotlib.pyplot as plt


def picture():
    price, size = numpy.loadtxt('house.csv', delimiter='|', usecols=(1, 2), unpack=True)
    plt.figure(2)
    plt.subplot(211)
    #plt.title("price")
    plt.title("/ 10000RMB")
    plt.hist(price, bins=20)

    plt.subplot(212)
    #plt.title("area")
    plt.xlabel("/ m**2")
    plt.hist(size, bins=20)
    plt.show()
