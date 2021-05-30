#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas
db = pandas.read_csv('marks.csv')
y = db["marks"]
x = db['hrs']
x = x.values
x = x.reshape(4,1)
from sklearn.linear_model import LinearRegression
mind = LinearRegression()
mind.fit( x,  y)
mind.predict([[ 6 ]] )
mind.coef_
import joblib
mind = joblib.load('marks.pk1')
y = int(input("enter no. of hours: "))
output = mind.predict([[y]])
print(output[0])

