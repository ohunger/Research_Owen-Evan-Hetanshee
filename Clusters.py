import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from pathlib import Path 

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

#No need to use the scaler since all columns should have identical range

x = df
x.drop(columns=["PublicID"], inplace=True)
x.drop(columns=["Unnamed: 0"], inplace=True)
x = x.fillna(0) # Have to double check this

pca_2 = PCA(n_components=2)   #12 dimensions to 2
pca_2_result = pca_2.fit_transform(x)
print('\n{:.2%} retained from dataframe after PCA \n'.format(np.sum(pca_2.explained_variance_ratio_)))
data_pca = pd.DataFrame(abs(pca_2.components_), columns=x.columns, index=['PC_1', 'PC_2'])
print(data_pca)

kmeans_model = KMeans()





