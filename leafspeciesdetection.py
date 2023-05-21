# -*- coding: utf-8 -*-
"""LeafSpeciesDetection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16fwzvyZK3wdMQVg0EOve_b6l3rrPKKys

# Importing Libraries
"""

import numpy as nm
import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

"""# Loading dataset"""

dataset = load_iris()

"""# Summarize Dataset"""

print(dataset.data)
print(dataset.target)
print(dataset.data.shape)

"""# Segregating data into X and Y"""

X=pd.DataFrame(dataset.data,columns=dataset.feature_names)
X

Y=dataset.target
Y

"""# Splitting Dataset into train and test"""

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(X,Y,test_size=0.25,random_state=0)
print(X_train.shape)
print(X_test.shape)

"""# Finding best max_depth

"""

accuracy=[]
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
for i in range(1,10):
  model = DecisionTreeClassifier(max_depth=i,random_state=0)
  model.fit(X_train,y_train)
  pred=model.predict(X_test)
  score=accuracy_score(y_test,pred)
  accuracy.append(score)

plt.figure(figsize=(12,6))
plt.plot(range(1,10),accuracy,color='red',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=10)
plt.title("Finding best max_depth")
plt.xlabel("pred")
plt.ylabel("score")

"""# Training"""

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
model.fit(X_train,y_train)

"""# Prediction"""

y_pred=model.predict(X_test)
print(nm.concatenate((y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),1))

"""# Accuracy Score"""

from sklearn.metrics import accuracy_score
print("Accuracy of the Model {0} ".format(accuracy_score(y_pred,y_test)*100))

"""# Visualizing Tree"""

from sklearn import tree
tree.plot_tree(model)