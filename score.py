import numpy as np
import pandas as pd
from itertools import combinations
from pathlib import Path 
# !!! Put CMA File in Same Directory as this file !!!

csv1 = Path(__file__).with_name('CMA.CSV') #fixed so you dont have to change address
df = pd.read_csv(csv1)

print('\nCMA CSV \n')

time = ['Prior to pregnancy:', 'During pregnancy:', 'Postpartum:']
letters = ['a','b','c']

#df2 = pd.DataFrame()
for i in range(3):
    print('# Treated for - Depression - {}'.format(time[i]), len(df[(df['CMAE04a1{}'.format(letters[i])] == 1.0)]))
    #df2['Depression - {}'.format(time[i])] = [ len(df[(df['CMAE04a1{}'.format(letters[i])] == 1.0)]) ]
print()
for i in range(3):
    print('# Treated for - Anxiety - {}'.format(time[i]), len(df[(df['CMAE04a2{}'.format(letters[i])] == 1.0)]))
    #df2['Anxiety - {}'.format(time[i])] = [ len(df[(df['CMAE04a2{}'.format(letters[i])] == 1.0)]) ]
print()
#print(df2)

#df1 = pd.DataFrame({'CMAE04a1a': df['CMAE04a1a'],'CMAE04a1b': df['CMAE04a1b'],'CMAE04a1c': df['CMAE04a1c']})
#print(df1.head())
#print(len(df1[(df1['CMAE04a1a'] == 1.0)]))   Works


print()

