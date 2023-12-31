# -*- coding: utf-8 -*-
"""Major_proj2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Td6K-uPJ_V5ZcLbmfVVMVyGr274j4Hxc
"""

import pandas as pd
df = pd.read_csv('/content/Fish.csv')
df

df.shape

df.size #Total number of elements in dataframe

df.info() #It gives the complete information about the dataframe

#to check the null values officially
df.isnull().sum()

#I want to find out the exact count of unique elements in each and every column
df.nunique()

#VISUALISATION - SEABORN
import seaborn as sns #import the library
sns.countplot(x = 'Species',data = df)

#I want the exact count of species
df['Species'].value_counts()

df['Species'].describe()

df.plot(x='Length1', y='Length3', kind='scatter')

df.plot(x='Length1', y='Length2', kind='scatter')

df.plot(x='Length2', y='Length3', kind='scatter')

#This function can be used to compute pairwise correlation of columns, excluding NA/null values.
df.corr()

#This function can be used to create pivot tables, which are useful for summarizing data and identifying patterns in the data.
pivot = df.pivot_table(index = ['Species'], values=['Height'], aggfunc ='sum')
pivot

#This function can be used to create pivot tables, which are useful for summarizing data and identifying patterns in the data.
pivot = df.pivot_table(index = ['Species'], values=['Height'], aggfunc =['sum','median','min'])
pivot

#Return those species whose value is between the given range of height
df.query('6 > Height > 5 and Weight > 200')