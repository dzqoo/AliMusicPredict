# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:08:49 2016

@author: root
"""
from datetime import datetime
import csv

reader = csv.reader(open('train_after_modify','r'))
writer = csv.writer(open('./data/train','w'))
i = 0
for item in reader:
#    print(item)
    if int(item[0][0:4]) < 1990:
        item[0] = 0
    elif 1990<=int(item[2][0:4])<2000:
        item[0] = 1
    elif 2000<=int(item[2][0:4])<2010:
        item[0] = 2
    else:
        item[0] = 3
    year = item[5][0:4]
    month = item[5][4:6]   
    day = item[5][6:8]
#    print(year)
#    print(month)
#    print(day)
#    del item[0]
#    del item[4]
#    del item[0]
#    del item[4]
    dayOfweek = datetime(int(year),int(month),int(day)).weekday()
    item[len(item)-1] = dayOfweek
    item[len(item)-1],item[len(item)-2] = item[len(item)-2],item[len(item)-1]
    writer.writerow(item)
    i +=1
    print(i)
print("num of record is %d" % i)
print("success!")