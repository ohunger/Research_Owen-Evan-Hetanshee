import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from pathlib import Path 
from sklearn.preprocessing import StandardScaler

## IMPORT from previous py
csv = Path(__file__).with_name('Markers.CSV')
df = pd.read_csv(csv)

#TODO: 1. ML K-Means Cluster (5-10 clusters)
#      2. How to Display, with multiple var, Axis??
#      3. Double Check clusters with display etc.

"""  VIA Korpusik:
To quickly answer your questions, you can use k-means for higher-dimensional data. 
Distance metrics like Euclidean distance work for higher dimensional arrays too! 
Just a reminder that you don't have to implement clustering from scratch since tools like sklearn have it already built in for you. 
If you ever need to reduce higher dimensional arrays to 2D or 3D, you can use tsne or pca. 
Hetanshee has experience using these tools and can show you how they work!
"""

x= df
x.drop(columns=["PublicID"], inplace=True)  #dropping non int columns
x.drop(columns=["Unnamed: 0"], inplace=True)
x = x.fillna(0) # Have to double check this
x = StandardScaler().fit_transform(x)

pca_2 = PCA(n_components=2)   #double check n_components
pca_2_result = pca_2.fit_transform(x)
print('\n{:.2%} retained from dataframe after PCA \n'.format(np.sum(pca_2.explained_variance_ratio_)))

data_pca = pd.DataFrame(pca_2_result)
print(data_pca)

plt.scatter(data_pca[0], data_pca[1], alpha=.1, color='black')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()



"""
      #had implemented this to see graph
features = range(pca_2.n_components_)
plt.bar(features, pca_2.explained_variance_ratio_, color='black')
plt.xlabel('PCA features')
plt.ylabel('variance %')
plt.xticks(features)
plt.show()
"""

kmeans_model = KMeans()





