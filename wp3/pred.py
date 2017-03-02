#! /usr/bin/python
import numpy as np
import xgboost as xgb


train= np.loadtxt('./data2/merged',delimiter=',')
print('train data is loaded successfully!')
pred= np.loadtxt('./data2/pred',delimiter=',')
print('pred data is loaded successfully!')



print(train.shape)
print(pred.shape)

train_x = train[:,0:8]
train_y = train[:,8]

pred_x = pred[:,0:8]
pred_y = pred[:,8]

xg_train = xgb.DMatrix(train_x,label = train_y)
xg_pred = xgb.DMatrix(pred_x,label = pred_y)
xg_train.save_binary('xg_train.buffer')

param={}
param['objective'] = 'multi:softprob'

param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 4

watchlist = [ (xg_train,'train'), (xg_pred, 'pred') ]
num_round = 5

bst = xgb.train(param, xg_train, num_round, watchlist );

bst.save_model('xgb.model')

pred = bst.predict(xg_pred);

np.savetxt('./data/pred.txt',pred,fmt="%d")
    
print('success!')


