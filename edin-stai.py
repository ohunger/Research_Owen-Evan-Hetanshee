import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path 

csv1 = Path(__file__).with_name('V1C.CSV')  #EDIN
dfe = pd.read_csv(csv1)
csv2 = Path(__file__).with_name('V1H.CSV')  #STAI
dfs = pd.read_csv(csv2)
csv3 = Path(__file__).with_name('CMA.CSV')  #3dep3anxiety
dfp = pd.read_csv(csv3)


def freqTable(): #crappy frequency table for edinburgh
    dict1 = {'varID' : ['V1CA01','V1CA02','V1CA03','V1CA04','V1CA05','V1CA06','V1CA07','V1CA08','V1CA09','V1CA10'], 1:[],2:[],3:[],4:[]}
    for i in range(1,11): #1-10
        for j in range(1,5): #Questions 1-4
            if(i>=10):
                dict1[j].append(len(dfe[(dfe['V1CA{}'.format(i)] == j)]))
            else:
                dict1[j].append(len(dfe[(dfe['V1CA0{}'.format(i)] == j)]))
    dict1 = pd.DataFrame(dict1)
    print(dict1,'\n')

def f(row): # TODO: || EDINBURGH || TOTAL SCORES COLUMN
    score = 0
    for i in range(1,11):
        if(i== 10):    
            score += abs(row['V1CA10'] - 4)  
        elif(i == 1 or i == 2 or i == 4): # 0,1,2,3   1,2,3,4
            score += row['V1CA0{}'.format(i)] - 1
        else: score += abs(row['V1CA0{}'.format(i)] - 4)
    return score

def v1(row): # TODO: || STAI || TOTAL SCORES COLUMN
    reverse = [1,3,6,7,10,13,14,16,19]
    score = 0
    for i in range(1,21):
            if(i>9):  
                if(i in reverse):
                    score += abs(row['V1HA{}'.format(i)] - 5) 
                else:  score += row['V1HA{}'.format(i)] 
            else:
                if(i in reverse):
                    score += row['V1HA0{}'.format(i)] 
                else: score += row['V1HA0{}'.format(i)]
    return score

def subEdinburgh(row): # || EDINBURGH || subscore if>=10: 1, 0 otherwise
    score = 0
    if(row['TotalEDINScore'] >= 10): score = 1
    return score

def suicidality(row): # || EDINBURGH || #want to double check with prof
    score = 0
    if(row['V1CA10']<=3): score = 1
    return score
    
def subSTAI(row): # || STAI ||  subscore if>=40: 1, 0 otherwise
    score = 0
    if(row['TotalSTAIScore'] >= 40): score = 1
    return score

def histo(): # TODO: HISTOGRAMS void function
    hist1 = dfe.hist(column='TotalEDINScore')
    plt.title('Edinburgh TotalScore')
    hist2 = dfs.hist(column='TotalSTAIScore')
    plt.title('STAI TotalScore')
    plt.show()

def newSet(row): #Trying to make descriptive 

    pass


def main():
    #freqTable()
    dfe['TotalEDINScore'] = dfe.apply(f, axis=1)    
    dfe['SubEDINScore'] = dfe.apply(subEdinburgh, axis=1)
    dfe['Suicidality'] = dfe.apply(suicidality, axis=1)
    #print('\n Edinburgh \n' )
    #print(dfe.head())

    
    dfs['TotalSTAIScore'] = dfs.apply(v1, axis=1) 
    dfs['SubSTAIScore'] = dfs.apply(subSTAI, axis=1)
    #print('\n STAI \n')
    #print(dfs.head())

    print('\n   GUIDE:')
    print('SubEdinScore (1 if>=10 )   SubSTAIScore (1 if>=40)  Suicidality(endorsed #10 Edinburgh')
    print('CMAE04a1 (a,b,c) = 1 if treated for depression.  CMAE04a2 (a,b,c) = 1 if treated for anxiety \n')
    

    dff = pd.DataFrame()
    dff = pd.merge(pd.merge(dfe,dfs, on="PublicID"),dfp,on="PublicID")
    dff = dff[['PublicID', 'SubEDINScore', 'SubSTAIScore', 'Suicidality', 'CMAE04a1a', 'CMAE04a1b','CMAE04a1c','CMAE04a2a','CMAE04a2b','CMAE04a2c']]
    #print(len(dff['PublicID']))
    print(dff.head())




main()
