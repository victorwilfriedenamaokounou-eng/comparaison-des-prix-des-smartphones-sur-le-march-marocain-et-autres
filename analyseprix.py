import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import missingno as msno
import openpyxl as xl
from sklearn.cluster import k_means, KMeans
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
print(df2.info())
print(df2)
print(df1.info())


t1=df2.stockage.tolist()
t2=df1.stockage.tolist()
t3=df2.RAM.tolist()
t4=df1.RAM.tolist()
t5=df2.prix.tolist()
t6=df1.prix.tolist()
tableau=np.array([t1,t3,t5]).T
print(tableau)
tableau1=np.array([t2,t4,t6]).T
print(tableau1)
model=KMeans(n_clusters=2)
model.fit(tableau1)
ypredict=model.predict(tableau1)
#plt.scatter(tableau1[:,0],tableau1[:,2],c=ypredict)
plt.scatter(tableau1[:,0],tableau1[:,2],c=ypredict)
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,2])
plt.scatter(model.cluster_centers_[:,1],model.cluster_centers_[:,2])
plt.show()


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
print(df2.info())
print(df2)
print(df1.info())


t1=df2.stockage.tolist()
t2=df1.stockage.tolist()
t3=df2.RAM.tolist()
t4=df1.RAM.tolist()
t5=df2.prix.tolist()
t6=df1.prix.tolist()
tableau=np.array([t1,t3,t5]).T
print(tableau)
tableau1=np.array([t2,t4,t6]).T
print(tableau1)
model=KMeans(n_clusters=2)
model.fit(tableau1)
ypredict=model.predict(tableau1)
#plt.scatter(tableau1[:,0],tableau1[:,2],c=ypredict)
plt.scatter(tableau1[:,0],tableau1[:,2],c=ypredict)
plt.scatter(model.cluster_centers_[:,0],model.cluster_centers_[:,2])
plt.scatter(model.cluster_centers_[:,1],model.cluster_centers_[:,2])
plt.show()