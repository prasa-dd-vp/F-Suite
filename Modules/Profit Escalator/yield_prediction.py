# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:46:13 2018

@author: prasad
"""

# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('tamilnadu_dataset.csv')

temp = pd.get_dummies(dataset['Season'])
dataset = dataset.drop(['Season'], axis =1)
dataset = dataset.join(temp)
X = dataset.iloc[:, [5]].values
y = dataset.iloc[:, 6].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.26, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print("Enter the area")
area = int(input())

regressor.predict(np.array([[area]]))
