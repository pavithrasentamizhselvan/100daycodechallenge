import numpy
import pandas
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
import pickle
'''Converts array into rows and columns'''
arr=numpy.array([[1,2,3],[4,5,6],[7,8,9]])
row=['a','b','c']
col=['one','two','three']
data=pandas.DataFrame(arr,index=row,columns=col)
print(data)
'''Using ridge to improve accuracy'''
'''dia.csv is the filename mine'''
url='dia.csv'
data=pandas.read_csv(url)
array=data.values
X=array[:,0:8]
Y=array[:,8]
scaler=StandardScaler().fit(X)
print(scaler)
print("REscale")
rescale=scaler.transform(X)
print(rescale)
numpy.set_printoptions(precision=3)
print(rescale[0:5,:])
print("Evaluation")
alphas=numpy.array([1,0.1,0.01,0.001,0.0001,0])
param_grid=dict(alpha=alphas)
modelg=Ridge()
grid=GridSearchCV(estimator=modelg,param_grid=param_grid)
grid.fit(X,Y)
print(grid.best_score_)
print(grid.best_estimator_.alpha)
'''COMPARING MODELS'''
models=[]
names=[]
res=[]
score='accuracy'
models.append(('L',LogisticRegression()))
models.append(('LDA',LinearDiscriminantAnalysis()))
for name,model in models:
#model=RandomForestClassifier(n_estimators=100,max_features=3)
    kfold=KFold(n_splits=10,random_state=7)
    cvres=cross_val_score(model,X,Y,cv=kfold)
    res.append(cvres)
    names.append(name)
    print("Accuracy  %3f (%3f)"%(cvres.mean(),cvres.std()))

pickle.dump(models[0],open('model.txt','wb'))
loa=pickle.load(open('model.txt','rb'))
print(loa)

     
     
