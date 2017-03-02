# -*- coding: utf-8 -*-
"""
Created on Tue May 17 09:41:28 2016

@author: root
"""
import time
str = 1426406400
value = time.localtime(str)
format = '%Y-%m-%d  %H:%M:%S'
dt = time.strftime(format,value)
print(dt)
