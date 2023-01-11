import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pathlib import Path 


## IMPORT from previous py
csv = Path(__file__).with_name('Markers.CSV')
df = pd.read_csv(csv)

#TODO: 1. ML K-Means Cluster (5-10 clusters)
#      2. How to Display, with multiple var, Axis??
#      3. Double Check clusters with display etc.

x = df
x.drop(columns=["PublicID"], inplace=True)
x.drop(columns=["Unnamed: 0"], inplace=True)
print(x.head())


