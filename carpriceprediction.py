# -*- coding: utf-8 -*-
"""CarPricePrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18noOTs1g9ChIXW2JKTimqhM4_zzGB-Hb

# Importing libraries
"""

import pandas as pd

"""# Load Dataset from Directory"""

from google.colab import files
uploaded=files.upload()

dataset=pd.read_csv("dataset.csv")
dataset=dataset.drop(['car_ID'],axis=1)

"""# Summarize data"""

print(dataset.shape)
print(dataset.head(5))

"""# Splitting data into X and Y"""

Xdata=dataset.drop('price',axis='columns')
numcols=Xdata.select_dtypes(exclude=['object']).columns
X=Xdata[numcols]
X

Y=dataset['price']
Y

"""# Scaling the Independent variables"""

from sklearn.preprocessing import scale
cols=X.columns
X=pd.DataFrame(scale(X))
X.columns=cols
print(X)

"""# Splitting data into train and test """

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.20,random_state=0)

"""# Training"""

from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor()
model.fit(X_train,y_train)

"""# Evaluating graph"""

y_pred=model.predict(X_test)
from sklearn.metrics import r2_score
r2score=r2_score(y_test,y_pred)
print("R2 score : ",r2score*100)