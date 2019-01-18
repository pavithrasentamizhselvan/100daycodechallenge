import sklearn
import pandas as pd
import numpy as np
from sklearn.model_selection import KFold,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df=pd.read_csv('dia.csv')
values=df.values
x=values[:,0:8]
y=values[:,8]
trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.2,random_state=7)
reg=LogisticRegression()
reg.fit(x,y)
'''predicts test data'''
result=reg.predict(testx)
print('Predicted result on test data',result)
kfold=KFold(n_splits=10,random_state=7)
score=cross_val_score(reg,x,y,cv=kfold)
res=reg.predict([[6,148,72,35,0,33.6,0.627,50]])
print('Test result on unknown data',res)
'''Evaluation'''
print(score)
'''End,try this by downloading diabetes dataset'''
