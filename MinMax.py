#coding:utf-8
from sklearn import preprocessing
import numpy as np
#初始化数据，每一行表示一个样本，每一列表示一个特征
x  = np.array([[0.,-3.,1.],
               [3.,1.,2.],
               [0.,1.,-1.]])
y = np.array([[5000.],[16000.],[58000.]])
#将数据进行[0,1]规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
minmax_y = min_max_scaler.fit_transform(y)
print (minmax_x)
print (minmax_y)
