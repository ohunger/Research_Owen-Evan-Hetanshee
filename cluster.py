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









