#! /usr/bin/python
import numpy as np
import xgboost as xgb


test= np.loadtxt('./data/test',delimiter=',')
print('test data is loaded successfully!')
train= np.loadtxt('./data/train',delimiter=',')
print('train data is loaded successfully!')


print(train.shape)
print(test.shape)


train_x = train[:,0:5]
train_y = train[:,5]

test_x = test[:,0:5]
test_y = test[:,5]


xg_train = xgb.DMatrix(train_x,label = train_y)
xg_test = xgb.DMatrix(test_x,label = test_y)
xg_test.save_binary('xg_test.buffer')

param={}
param['objective'] = 'multi:softmax'

param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 4

watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
num_round = 5

bst = xgb.train(param, xg_train, num_round, watchlist );

bst.save_model('xgb.model')

pred = bst.predict(xg_test);

np.savetxt('./data/pred.txt',pred,fmt="%d")
    
i = 0

print ('predicting, classification error=%f' % (sum( int(pred[i]) != test_y[i] for i in range(len(test_y))) / float(len(test_y)) ))













































# label need to be 0 to num_class -1
#data = np.loadtxt('./dermatology.data', delimiter=',',converters={33: lambda x:int(x == '?'), 34: lambda x:int(x)-1 } )
#sz = data.shape
#
#train = data[:int(sz[0] * 0.7), :]
#np.savetxt("train.txt",train,fmt="%d")
#test = data[int(sz[0] * 0.7):, :]
#np.savetxt("test.txt",test,fmt="%d")
##print(data.shape)
#print(train.shape)
##print(test.shape)
#train_X = train[:,0:33]
#train_Y = train[:, 34]
#print(train_Y)
#
#test_X = test[:,0:33]
#test_Y = test[:, 34]
#
#xg_train = xgb.DMatrix( train_X, label=train_Y)
#xg_test = xgb.DMatrix(test_X, label=test_Y)
#
#
#la_tr = xg_train.get_label()
#print(la_tr.size)
#la_te = xg_test.get_label()
#print(la_te.size)
#
##for i in range(len(la_te)):
##    print(la_te[i])
## setup parameters for xgboost
#param = {}
## use softmax multi-class classification
#param['objective'] = 'multi:softmax'
## scale weight of positive examples
#param['eta'] = 0.1
#param['max_depth'] = 6
#param['silent'] = 1
#param['nthread'] = 4
#param['num_class'] = 6
#
#watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
#num_round = 5
#bst = xgb.train(param, xg_train, num_round, watchlist );
## get prediction
#pred = bst.predict( xg_test );
#i = 0
##for i in range(len(pred)):
##    print(pred[i])
#
#print ('predicting, classification error=%f' % (sum( int(pred[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y)) ))
#
## do the same thing again, but output probabilities
#param['objective'] = 'multi:softprob'
#bst = xgb.train(param, xg_train, num_round, watchlist );
## Note: this convention has been changed since xgboost-unity
## get prediction, this is in 1D array, need reshape to (ndata, nclass)
#yprob = bst.predict( xg_test ).reshape( test_Y.shape[0], 6 )
#ylabel = np.argmax(yprob, axis=1)
#
#print ('predicting, classification error=%f' % (sum( int(ylabel[i]) != test_Y[i] for i in range(len(test_Y))) / float(len(test_Y))))