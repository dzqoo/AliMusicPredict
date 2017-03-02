# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:55:12 2016

@author: root
"""


flist = ['./data0/1','./data0/2']
ofile = open('./data0/merged','w')

fmap = {}
i = 0
j = 0
for fl in flist:
    i += 1 
    for txt in open(fl,'r'):
        ofile.write(txt)
        j += 1 
        print(j)
    fmap[i] = j
    j = 0 
ofile.close()

print('the record num of 1 is %d' % fmap[1])
print('the record num of 2 is %d' % fmap[2])
print('the record num of merged is %d' % (fmap[1]+fmap[2]))



