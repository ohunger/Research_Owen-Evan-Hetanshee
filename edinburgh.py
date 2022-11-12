import numpy as np
import pandas as pd
from pathlib import Path 

csv1 = Path(__file__).with_name('V1C.CSV') #fixed so you dont have to change address
df = pd.read_csv(csv1)

print('\n Edinburgh Postnatal Depression Scale - #ppl that answered each checkbox \n')
dict1 = {'varID' : ['V1CA01','V1CA02','V1CA03','V1CA04','V1CA05','V1CA06','V1CA07','V1CA08','V1CA09','V1CA10'], 1:[],2:[],3:[],4:[]}
for i in range(1,11): #1-10
    for j in range(1,5): #Questions 1-4
        if(i>=10):
            dict1[j].append(len(df[(df['V1CA{}'.format(i)] == j)]))
        else:
            dict1[j].append(len(df[(df['V1CA0{}'.format(i)] == j)]))
dict1 = pd.DataFrame(dict1)
print(dict1,'\n')

# TODO: EDINBURGH TOTAL SCORES

def f(row):
    score = 0
    for i in range(1,11):
        if(i== 10):    
            score += abs(row['V1CA10'] - 4)
        elif(i == 1 or i == 2 or i == 4):
            score += row['V1CA0{}'.format(i)] - 1
        else: score += abs(row['V1CA0{}'.format(i)] - 4)
    return score

df['TotalScore'] = df.apply(f, axis=1)
print(df.head())
print('\n Mean Total Score:', df['TotalScore'].mean() ,'\n')






