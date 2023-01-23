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


def main():
    x = df
    x.drop(columns=["PublicID"], inplace=True)  #dropping non int columns
    x.drop(columns=["Unnamed: 0"], inplace=True)
    x = x.fillna(0) 
    plottin(x)
    #x = StandardScaler().fit_transform(x)


def plottin(dataf):
    copy = pd.DataFrame({'Variables':['SubEDINScore', 'SubSTAIScore', 'Suicidality', 'CMAE04a1a', 'CMAE04a1b','CMAE04a1c','CMAE04a2a','CMAE04a2b','CMAE04a2c','ADHD','OCD','panic disorder'],'Endorsement':[0,0,0,0,0,0,0,0,0,0,0,0]})
    i = 0
    for (columnName, columnData) in dataf.items():
        copy['Endorsement'].iat[i] = len(dataf[dataf[columnName]==1])/len(dataf[columnName])
        i+=1
        #realized i coulda just done mean here woops
        pass
    print(copy)
    
    ax = copy.plot.line(x='Variables', y='Endorsement', rot=0,figsize=(14,6),
        fontsize=9, marker = 'o', linestyle = '--',
        title = "Variables vs % Endorsement",grid=True,xticks=copy.index,
        xlabel = 'Variables',ylabel = 'Percent Endorsement')
        
    
    plt.show()
    """
    
    plt.plot(copy.columns, copy.columnData, marker = 'o', linestyle = '--')
    plt.title('Explained Variance by Componenets')
    plt.xlabel("Variables")
    plt.ylabel("Percent Endorsement")
    plt.show()
    """
    pass

main()





