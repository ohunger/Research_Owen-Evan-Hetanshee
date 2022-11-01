import numpy as np
import pandas as pd
from pathlib import Path 

"""
TODO: Create total score on Edinburgh scale

X Frequency Table of total scores ()
X for every score, the number of people who scored each 

Depression and Anxiety combination: get
average and range of depression and anxiety range
"""

csv1 = Path(__file__).with_name('V1C.CSV') #fixed so you dont have to change address
df = pd.read_csv(csv1)

print('\n Edinburgh Postnatal Depression Scale - #ppl for every score \n')
dict1 = {'ID' : ['V1CA01','V1CA02','V1CA03','V1CA04','V1CA05','V1CA06','V1CA07','V1CA08','V1CA09','V1CA10'], 1:[],2:[],3:[],4:[]}
temp = []
for i in range(1,11):
    for j in range(1,5):
        if(i>=10):
            dict1[j].append(len(df[(df['V1CA{}'.format(i)] == j)]))
        else:
            dict1[j].append(len(df[(df['V1CA0{}'.format(i)] == j)]))
dict1 = pd.DataFrame(dict1)
print(dict1,'\n')





# Both below work just wanted correct format and not just value_counts for each
"""
for i in range(1,11):
    if(i>=10):
        print(df['V1CA{}'.format(i)].value_counts())
    else:
        print(df['V1CA0{}'.format(i)].value_counts())
    print()
print()
"""

"""
for i in range(1,11):
    for j in range(1,5):
        if(i>=10):
            print('#ppl scored {} V1CA{}:'.format(j,i), len(df[(df['V1CA{}'.format(i)] == j)]),'', end ='')
        else:
            print('#ppl scored {} V1CA0{}:'.format(j,i), len(df[(df['V1CA0{}'.format(i)] == j)]),'', end ='')
    print()

print()
"""