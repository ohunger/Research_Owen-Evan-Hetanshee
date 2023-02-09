from sklearn.cluster import KMeans
import numpy as np
import random
from datetime import datetime
from matplotlib import cm
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D

csv = Path("kmeans").with_name('Markers.CSV')
df = pd.read_csv(csv)

X = df
X.drop(columns=["PublicID"], inplace=True)  # dropping non int columns
X.drop(columns=["Unnamed: 0"], inplace=True)
X = X.fillna(0)  # Have to double check this
data = X
wcss = []  # sum of square

for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42).fit(X)
        wcss.append(kmeans.inertia_)

plt.plot(range(1, 10), wcss)
plt.title('The Elbow Graph')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

#clustering
kmeans = KMeans(n_clusters=6, init='k-means++', max_iter=300, n_init=10, random_state=0).fit(X)


data['clusters'] = kmeans.labels_
y= data['clusters']

# colors = ['red', 'blue', 'green', 'magenta', 'yellow', 'cyan', 'hotpink', 'purple']
# data['c']= data.clusters.map({0:colors[0], 1:colors[1],2:colors[2], 3:colors[3], 4:colors[4], 5:colors[5], 6:colors[6], 7:colors[7]})

###########  
# kmeans = KMeans(n_clusters=7, random_state=0).fit(x_onehot)
# result = []
# for i in range(len(x_onehot)):
#         result.append([x_onehot[i],kmeans.labels_[i]])
# display(result, 'Kmeans')

# labels = popc(x_onehot)
# result = []
# for i in range(len(x_onehot)):
#         result.append([labels[i], x_onehot[i]])
# display(result, 'POPC')

# from sklearn.cluster import SpectralClustering
# from sklearn.metrics import jaccard_score
#
#
# # Convert the pandas DataFrame to a NumPy array
# data = data.values
#
# # Define the number of clusters
# n_clusters = 8
#
# # Perform Spectral Clustering on the binary data
# spectral_clustering = SpectralClustering(n_clusters=n_clusters, affinity='rbf')
#
# labels = spectral_clustering.fit_predict(data)
# print(labels)
# # Calculate the Jaccard similarity between each pair of binary vectors
# jaccard = np.zeros((data.shape[0], data.shape[1]))
# for i in range(data.shape[0]):
#     for j in range(i, data.shape[1]):
#         jaccard[i, j] = jaccard_score(data[i], data[j])
#         jaccard[j, i] = jaccard[i, j]
#
# # Evaluate the similarity between patients in each cluster
# # for i in range(n_clusters):
# #     cluster_indices = np.where(labels == i)[0]
# #     cluster_similarity = np.mean(jaccard[np.ix_(cluster_indices, cluster_indices)])
# #     if cluster_similarity != 0:
# #         print(f'Cluster {i} mean Jaccard similarity: {cluster_similarity:.2f}')
