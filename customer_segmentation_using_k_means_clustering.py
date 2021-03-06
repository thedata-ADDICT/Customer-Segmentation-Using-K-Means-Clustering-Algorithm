# -*- coding: utf-8 -*-
"""Customer Segmentation Using K-Means Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_W6Pg4ST210NwRWkuJ5zO3Q5eNBtg_8J

# Importing the Neccessary Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

"""# Data Collection and Analysis"""

# Loading the CSV Data File into a Pandas Dataframe
df = pd.read_csv('/Mall_Customers.csv')
print("Data File Successfully Loaded into CSV")

# Printing the first 5 rows of DataFrame
df.head()

# Finding the number of rows and columns
df.shape

# Getting some informations about the dataset
df.info()

# Getting Info about Null Data 
df.isnull().sum()

"""# Selecting the Anual Income and Spending Column """

X = df.iloc[:,[3,4]].values
print(X)

"""# Finding the optimal value of K (Clusters) using WCSS Method (Elbow Method) """

# Finding WCSS value for different number of clusters

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(X)

  wcss.append(kmeans.inertia_)

# Printing the WCSS Value
print(wcss)

# Plotting the Elbow Graph

sns.set()
plt.plot(range(1,11), wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

"""Seeing the above graph we can conclude that optimum value of K would be 5 

Hence our Cluster group would be 0,1,2,3,4

# Training the K Means Model with K=5
"""

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)

# Return a label for each data point based on their cluster
Y = kmeans.fit_predict(X)

print(Y)

"""# Visualising the Clusters"""

# Plotting all the clusters 

plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0], X[Y==0,1], s=30, c='green', label='Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=30, c='red', label='Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=30, c='yellow', label='Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=30, c='pink', label='Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=30, c='violet', label='Cluster 5')

# Plotting the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='black', label='Centroids')

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()

"""# The above Graph shows the Customers coming to the mall identified into different clusters based on their Spending Amount and Annual Income"""

