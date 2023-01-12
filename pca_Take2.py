import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from pathlib import Path 
from sklearn.preprocessing import StandardScaler


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





kmeans_model = KMeans()

