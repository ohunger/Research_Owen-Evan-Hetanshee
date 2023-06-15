import pandas as pd
from pathlib import Path 

csv_file1 = Path(__file__).with_name('V1A.CSV')  # Load the CSV file
csv_file2 = Path(__file__).with_name('V3A.CSV')  # Load the CSV file
df1 = pd.read_csv(csv_file1)  # Read the CSV into a DataFrame
df2 = pd.read_csv(csv_file2)  # Read the CSV into a DataFrame

# Merge both dataframes
df = pd.merge(df1, df2, on="PublicID", how="outer")

def compute_scores(row):
    # Reverse score the necessary questions in the 1-5 range
    reverse_columns = ['V1AH04', 'V1AH05', 'V1AH07', 'V1AH08', 'V3AG04', 'V3AG05', 'V3AG07', 'V3AG08']
    row[reverse_columns] = 6 - row[reverse_columns]

    # Adjust scores from 1-5 to 0-4 for all questions
    pss_columns = ['V1AH{:02d}'.format(i) for i in range(1, 11)] + ['V3AG{:02d}'.format(i) for i in range(1, 11)]
    row[pss_columns] = row[pss_columns] - 1
    
    total_score = row[pss_columns].sum()
    return pd.Series({'TotalScore': total_score})

def stress_level(score):
    if 0 <= score <= 13:
        return 'low stress'
    elif 14 <= score <= 26:
        return 'moderate stress'
    elif 27 <= score <= 40:
        return 'high stress'
    else:
        return 'invalid score'

df = df.join(df.apply(compute_scores, axis=1))
df['StressLevel'] = df['TotalScore'].apply(stress_level)

# Select only the necessary columns
df = df[['PublicID', 'TotalScore', 'StressLevel']]

print(df)
stress_counts = df['StressLevel'].value_counts()
print(stress_counts)
