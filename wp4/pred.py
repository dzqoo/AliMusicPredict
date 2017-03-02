#! /usr/bin/python
import numpy as np
import xgboost as xgb


train= np.loadtxt('./data/train',delimiter=',')
print('train data is loaded successfully!')
pred= np.loadtxt('./data/pred',delimiter=',')
print('pred data is loaded successfully!')



print(train.shape)
print(pred.shape)

train_x = train[:,0:7]
train_y = train[:,7]

pred_x = pred[:,0:7]
pred_y = pred[:,7]

xg_train = xgb.DMatrix(train_x,label = train_y)
xg_pred = xgb.DMatrix(pred_x,label = pred_y)
xg_train.save_binary('xg_train.buffer')

param={}
param['objective'] = 'multi:softmax'

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


