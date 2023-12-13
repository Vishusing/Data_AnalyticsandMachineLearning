# -*- coding: utf-8 -*-
"""Major_project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HieFJy4bQcELOQbrSZAdmHcKvcDfJmVC

Importing the Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

"""Data Collection and Processing"""

# Loading the csv data to a Pandas DataFrame
gold_data = pd.read_csv('/content/gld_price_data.csv')
gold_data

# print first 5 rows of the dataframe
gold_data.head()

# print last 5 rows of the dataframe
gold_data.tail()

# Number of rows and columns
gold_data.shape

# getting some basic information about the data
gold_data.info()

# checking the no. of missing values
gold_data.isnull().sum()

# getting the statistical measure of the data
gold_data.describe()

"""Correlation
1. Positive Correlation
2. Negative Correlation
"""

correlation = gold_data.corr()

# Constructing a heat map to understand the correlation
plt.figure(figsize = (8,8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

# correlation values at gld
print(correlation['GLD'])

# checking the distribution of the GLD data
sns.distplot(gold_data['GLD'],color='green')

"""Splitting the Features and Target"""

X = gold_data.drop(['Date','GLD'],axis=1)
Y = gold_data['GLD']

print(X)

print(Y)

"""Splitting into Training data and Test Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=2)

"""Model Training: Random Forest Regressor"""

regressor = RandomForestRegressor(n_estimators=100)

#Training the model
regressor.fit(X_train,Y_train)

"""Model Evaluation"""

# Prediction on test data
test_data_prediction = regressor.predict(X_test)

print(test_data_prediction)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print('R squared error is:-', error_score)

"""Compare the Actual Values and Predicted Values in a Plot"""

Y_test = list(Y_test)

plt.plot(Y_test, color='blue', label='Actual Value')
plt.plot(test_data_prediction, color='green', label='Predicted Value')
plt.title('Actual Price Vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()