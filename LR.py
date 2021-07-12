# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:25:50 2020

@author: chait
"""

import pandas as pd

from matplotlib import pyplot as plt
 
df = pd.read_csv("Book1.csv")
df.head()
plt.scatter(df.temp,df.effect,marker='+',color='red')
df.shape 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(df[['temp']],df.effect,test_size=0.1)
from sklearn.linear_model import LogisticRegression
print(X_test)
print(X_train)
model=LogisticRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))