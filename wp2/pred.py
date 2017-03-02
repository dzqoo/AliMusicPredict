# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:53:06 2016

@author: root
"""
import xgboost as xgb
import numpy as np



bst = xgb.Booster(model_file='xgb.model')
dtest = xgb.DMatrix('xg_test.buffer')
pred = bst.predict(dtest);
np.savetxt('./data/pred.txt',pred,fmt="%d")
print('predicting is finished!')
    
