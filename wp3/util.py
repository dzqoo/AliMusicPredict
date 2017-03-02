# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:51:20 2016

@author: root
"""


import csv
#import random

#reader = csv.reader(open('./data0/handled','r'))
#i = 0
#for item in reader:
#    i +=1
#print(i)

reader = csv.reader(open('./data0/3','r'))
writer = csv.writer(open('./data0/3_handled','w'))
i = 0
for item in reader:
    if int(item[5][0:4]) < 1990:
        item[5] = 0
    elif 1990<=int(item[5][0:4])<1995:
        item[5] = 1
    elif 1995<=int(item[5][0:4])<2000:
        item[5] = 2
    elif 2000<=int(item[5][0:4])<2005:
        item[5] = 3
    else:
        item[5] = 4        
#    year = item[12][0:4]
#    month = item[12][4:6]   
#    day = item[12][6:8]
#    dayOfweek = datetime(int(year),int(month),int(day)).weekday()
#    item[12] = dayOfweek
    del item[0]
    del item[2]
    del item[2]
    del item[6]
    del item[6]
    item[len(item)-1],item[len(item)-2]  = item[len(item)-2],item[len(item)-1]
    writer.writerow(item)
    i +=1
    print(i)
print("num of record is %d" % i)
print("success!")

#reader = csv.reader(open('./data0/1_handled','r'))
#writer = csv.writer(open('./data0/1_handled1','w'))
#i = 0
#for item in reader:
#    del item[0]
#    writer.writerow(item)
#    i += 1
#    print(i)
#print("num of record is %d" % i)
#print("success!")

#reader = csv.reader(open('./data0/lhm','r'))
#writer = csv.writer(open('./data2/pred','w'))
#
#i = 0 
#for item in reader:
#    if int(item[2][0:4]) < 1990:
#        item[2] = 0
#    elif 1990<=int(item[2][0:4])<1995:
#        item[2] = 1
#    elif 1995<=int(item[2][0:4])<2000:
#        item[2] = 2
#    elif 2000<=int(item[2][0:4])<2005:
#        item[2] = 3
#    else:
#        item[2] = 4    
#    item.append(1)
#    writer.writerow(item)
#    i +=1
#    print(i)
#print("num of record is %d" % i)








