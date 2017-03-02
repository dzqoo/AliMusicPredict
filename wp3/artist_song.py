# -*- coding: utf-8 -*-
"""
Created on Thu May 19 14:01:37 2016

@author: root
"""

import csv

reader = csv.reader(open('./data0/src','r'))
writer = csv.writer(open('./data0/artist_song','w'))
writer0 = csv.writer(open('./data0/artist','w'))
artist = []
i = 0
j = 0
for item in reader:
    temp = item[0:2]
    temp0 = item[0:1]
    if temp[0] not in artist:
        j +=1
        artist.append(temp[0])
        print('artist is %d now' % j)
        writer0.writerow(temp0)
        print('artist is addone')
    writer.writerow(temp)
    i +=1
print('the total record is %d' % i)
print('the total arttist is %d' % j) 
print('song of artist is parsed successfully! ')

     