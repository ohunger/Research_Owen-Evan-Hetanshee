import numpy as np
import pandas as pd

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from pathlib import Path 
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

csv = Path(__file__).with_name('Markers.CSV')
df = pd.read_csv(csv)

x = df
x.drop(columns=["PublicID"], inplace=True)  #dropping non int columns
x.drop(columns=["Unnamed: 0"], inplace=True)
x = x.fillna(0) # Have to double check this

x = StandardScaler().fit_transform(x)
pca = PCA()   
pca.fit(x)
print("\n", pca.explained_variance_ratio_ ,"\n")

plt.figure(figsize=(10,8))
plt.plot(range(1,13), pca.explained_variance_ratio_.cumsum(), marker = 'o', linestyle = '--')
plt.title('Explained Variance by Componenets')
plt.xlabel("Num Componenents")
plt.ylabel('Cumulative Explained Variance')
plt.show()

#I picked 7 cause it was about above 80%, I think that is correct method
pca = PCA(n_components=7)
pca.fit(x)
scoresPCA = pca.transform(x)

wcss = [] #sum of square
for i in range(5,10):
    kmeans_pca = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans_pca.fit(scoresPCA)
    wcss.append(kmeans_pca.inertia_)

plt.figure(figsize=(10,8))
plt.plot(range(5,10), wcss, marker = 'o', linestyle = '--')
plt.title('optimal clusters')
plt.xlabel("Num Clusters")
plt.ylabel('wcss')
plt.show()

#Optinum clusters via plotting looks to be 8 
"""
kmeans_pca = KMeans(n_clusters = 8, init = 'k-means++', random_state=42)
kmeans_pca.fit(scoresPCA)

dfkmeans = pd.concat([df.reset_index(drop=True),pd.DataFrame(scoresPCA)], axis=1)
dfkmeans.columns.values[-3: ] = ['Component 1', 'Component 2', 'Component 3']
dfkmeans['Segment K-means'] = kmeans_pca.labels_
print(dfkmeans.head())
"""




