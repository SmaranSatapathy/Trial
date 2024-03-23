import pandas as pd
from sklearn.model_selection import train_test_split

data=pd.read_csv("new_data.csv")
print(data.info())

Y=data.iloc[:,0]
X=data.iloc[:,1:]

train_X, train_Y,test_X,test_Y=train_test_split(X,Y,test_size=0.3)

print(train_X.shape)
print(train_Y.shape)
print(test_X.shape)
print(test_Y.shape)