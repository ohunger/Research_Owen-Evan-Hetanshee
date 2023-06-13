import pandas as pd
from pathlib import Path

def compute_discrimination_scores(row):
    discrimination_columns = ['V2AG01', 'V2AG02', 'V2AG03a', 'V2AG03b', 'V2AG03c', 'V2AG03d', 'V2AG03e', 'V2AG03f', 'V2AG03g', 'V2AG03h', 'V2AG03i']
    row[discrimination_columns] = 4 - (row[discrimination_columns] - 1)
    total_score = row[discrimination_columns].sum()
    return pd.Series({'DiscriminationScore': total_score})

def discrimination_level(score):
    if score < 10:
        return 'Low Discrimination'
    elif score < 20:
        return 'Moderate Discrimination'
    else:
        return 'High Discrimination'

csv_file = Path(__file__).with_name('V2A.CSV')  # Load the CSV file
df = pd.read_csv(csv_file)  # Read the CSV into a DataFrame

df = df.join(df.apply(compute_discrimination_scores, axis=1))

df['DiscriminationLevel'] = df['DiscriminationScore'].apply(discrimination_level)

# Select only the necessary columns
df = df[['PublicID', 'DiscriminationScore', 'DiscriminationLevel']]

print(df)
discrimination_counts = df['DiscriminationLevel'].value_counts()
print(discrimination_counts)