import numpy as np
import pandas as pd

df = pd.read_csv('/Users/owenhunger/Documents/Research/CSV/CMA.CSV')

print('\nCMA DS \n')

print('How Many People fall into each diagnostic category: \n')
depression_Prior = df[(df['CMAE04a1a'] == 1.0)]
print('# Treated for - Depression - Prior to pregnancy:', len(depression_Prior))
depression_During = df[(df['CMAE04a1b'] == 1.0)]
print('# Treated for - Depression - During pregnancy:', len(depression_During))
depression_Postpartum = df[(df['CMAE04a1c'] == 1.0)]
print('# Treated for - Depression - Postpartum:', len(depression_Postpartum))
print('\n')
anxiety_Prior = df[(df['CMAE04a2a'] == 1.0)]
print('# Treated for - Anxiety - Prior to pregnancy:', len(anxiety_Prior))
anxiety_During = df[(df['CMAE04a2b'] == 1.0)]
print('# Treated for - Anxiety - During pregnancy:', len(anxiety_During))
anxiety_Postpartum = df[(df['CMAE04a2c'] == 1.0)]
print('# Treated for - Anxiety - Postpartum:', len(anxiety_Postpartum))
print('\n')


