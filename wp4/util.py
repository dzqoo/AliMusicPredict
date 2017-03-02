# -*- coding: utf-8 -*-
"""
Created on Sat May 21 14:53:15 2016

@author: root
"""
#1,merge files 
#fo = open('./data0/merged','w')
#
#smap = []
#for l in open ('./data0/merged'):
#    arr = l.split(',')
#    if arr[1] not in smap:
#        if int(arr[8]) == 1:
#             fo.write(arr[1])
#             fo.
#       

#import csv
#reader = csv.reader(open('./art/1','r'))
#writer = csv.writer(open('./art/1_handled','w'))
#
#for item in reader:
#    arr = item.sssss


#2,generate format libsvm input

#fo = open('./art/1_handled','w')
#i = 0
#for l in open('./art/1'):
#    arr = l.split(',')
#    print(arr)
#    for i in range(0,len(arr)-1):
#        fo.write('%d %d:%d'%(int(arr[i]),0,i+1))
#        fo.write('\n')
#        print(i)
#fo.close()
#print('the total days are %d'% (i+1))
        
#3,generate pred files

#import random as rd        
#
#i = 0
#j = 0
#k = 0
#for k in range(0,50):
#    k += 1
#    name = './arts/pred' + str(k)
#    fo = open(name ,'w')
#    for i in range(183,243):
#        fo.write('%d %d:%d'%(rd.randint(500,1000),0,i))
#        fo.write('\n')
#        j += 1
#        print(j)
#fo.close()
#print('the total days are %d' % j)
    
#4,generation total input files
#import time
#i = 0
#j = 0
#k = 0
#for l in open('./art/artist_all_play.txt'):
#    i += 1
#    print(l)
#    if i%2 == 0:
#        j += 1
#        arr = l.split(',')
#        name = './arts/train' + str(j)
#        fo = open(name,'w')
#        for i in range(0,len(arr)):
#            fo.write('%d %d:%d' % (int(arr[i]),0,i+1))
#            fo.write('\n')
#        i = 0
#        print('the input file %d is finished!' % j)
#        k += 1
#        fo.close()
#print('generate %d inputfiles' % k)
    
    
#5,mkdir

#import os 
#
#i = 0
#
#for i in range(1,51):
#    name ='./data2/'+str(i)
#    os.mkdir(name)
#    
    
    
#6,generate artists
#i = 0
#j = 1
#fo = open('./data1/artists','w')
#for l in open ('./art/artist_all_play.txt'):
#    i += 1
#    if i %2 != 0:        
#        fo.write('%s' % l)
#        print(j)
#        j += 1
#fo.close()       
    
#7,match the output with artists
#import time 
#import datetime
#fo = open('/home/dzq/dzq/wp3/data0/pred','w')
#arr = []
#i = 0 
#j = 0
#for l0 in open ('./data1/artists'):
#    i += 1
#    arr = l0.strip('\n')
#    name = '/home/dzq/dzq/wp3/data0/' + str(i) + '_result'
#    j += 1
#    timeStr='2015-09-01'
#    timeArray = time.strptime(timeStr,'%Y-%m-%d')
#    print(timeArray)
#    year = '2015'
#    month = '09'
#    day = '01'
#    for l1 in open(name):
#        temp = l1.strip('\n')
#        day_bf = int(float(temp))
#        monthTemp = month
#        if len(month) < 2:
#            monthTemp = '0' + month
#        dayTemp = day
#        if len(day) < 2:
#            dayTemp = '0' + day
#        fo.write('%s,%d,%s' % (arr,day_bf,year+monthTemp+dayTemp))
#        fo.write('\n')
#        times = datetime.datetime(int(year),int(month),int(day))+datetime.timedelta(1)
#        year = str(times.year)
#        month = str(times.month)
#        day =  str(times.day)
#print('the total artists is %d ' % j)
#    
    
    
#8, delete art
    
i = 0
j = 0
k = 0
for l in open('./art/artist_all_play.txt'):
    i += 1
    print(l)
    if i%2 == 0:
        j += 1
        arr = l.split(',')
        name = '/home/dzq/dzq/wp0/data0/' + str(j)
        fo = open(name,'w')
        for i in range(0,len(arr)):
            fo.write('%d' % (int(arr[i])))
            fo.write('\n')
        i = 0
        print('the input file %d is finished!' % j)
        k += 1
        fo.close()
print('generate %d inputfiles' % k)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   