import pandas as pd
import numpy as np
import openpyxl as xl
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import math
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer


df=pd.read_excel("classeur2.xlsx")
df1=pd.read_excel("classeur3.xlsx")
df2=df.drop(columns=['notusing'])
print(df2.head())
imputer=SimpleImputer(missing_values=np.nan, strategy='most_frequent')
df2[['brandimpute']]=imputer.fit_transform(df2[['brand']])
df2=df2.drop(columns=['brand'])
df2=df2.drop(columns=['name'])
imputer1=KNNImputer(n_neighbors=3)
df2[['stockage','RAM','prix']]=imputer1.fit_transform(df2[['stockage','RAM','prix']])
imputer2=KNNImputer(n_neighbors=4)
df1[['stockage','RAM','prix']]=imputer2.fit_transform(df1[['stockage','RAM','prix']])
print(df['brand'].value_counts())
print(df1['brand'].value_counts())