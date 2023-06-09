# -*- coding: utf-8 -*-
"""LogisticRegression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FaEdiC2GyeX-C_3cO29LqQL_Kb9rCrJ-

# **Predicting whether the customer buys a product by Age and Salary by using LogisticRegression **
"""

import pandas as pd #importing pandas to access dataset
import numpy as np #importing numpy to perform array calculations

#choose datafile from local directory
from google.colab import files
uploaded=files.upload()

#load dataset
dataset=pd.read_csv("DigitalAd_dataset.csv")

#summarizing dataset
print(dataset.shape)
print(dataset.describe())
print(dataset.head(5))

#seggregating data into independent varaible x
X=dataset.iloc[:,:-1].values
print(X)

#seggregating data into independent varaible y
Y=dataset.iloc[:,-1].values
print(Y)

#splitting data into train and test data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

#preprocessing of data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#training the data
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(random_state=0)
model.fit(X_train,y_train)

#testing our model
age=int(input("Enter Customers Age :"))
sal=int(input("Enter customer salary:"))
newcust=[[age,sal]]
result=model.predict(sc.transform(newcust))
print(result)
if result==1:
  print("Customer will buy the product")
else:
  print("customer will not buy the product")

y_pred=model.predict(X_test)
print(np.concatenate(y_pred.reshape(len(y_pred),1)),y_test.reshape(len(y_test),1))

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
print("confusion matrix:")
print(cm)
print("accuracy of the model :{0}%".format(accuracy_score(y_test,y_pred)*100))

from sklearn.metrics import roc_auc_score,roc_curve
from matplotlib import pyplot as plt
nsProb= [0 for _ in range(len(y_test))]
lsprob=model.predict_proba(X_test)
lsprob=lsprob[:,1]
nsAUC= roc_auc_score(y_test,nsProb)
lsAUC= roc_auc_score(y_test,lsprob)
print("No skill ROC_AUC=%.3f"%(nsAUC*100))
print("Logistic skill skill ROC_AUC=%.3f"%(lsAUC*100))
nsFP,nsTP=roc_curve(y_test,nsProb)
lsFP,lsTP=roc_curve(y_test,lsprob)
plt.plot(nsFP,nsTP,linestyle="--",label="no skill")
plt.plot(lsFP,lsTP,linestyle="--",label="Logistic skill")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold