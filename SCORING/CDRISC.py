import pandas as pd
from pathlib import Path 

csv_file = Path(__file__).with_name('V2I.CSV')  # Load the CSV file
df = pd.read_csv(csv_file)  # Read the CSV into a DataFrame

def compute_resilience_scores(row):
    resilience_columns = ['V2IA{:02d}'.format(i) for i in range(1, 26)]
    # Adjust scores from 1-5 to 0-4
    row[resilience_columns] = row[resilience_columns] - 1
    total_score = row[resilience_columns].sum()
    return pd.Series({'ResilienceScore': total_score})

def resilience_level(score):
    if score < 50:
        return 'Low Resilience'
    elif score < 75:
        return 'Moderate Resilience'
    else:
        return 'High Resilience'

df = df.join(df.apply(compute_resilience_scores, axis=1))
df['ResilienceLevel'] = df['ResilienceScore'].apply(resilience_level)

# Select only the necessary columns
df = df[['PublicID', 'ResilienceScore', 'ResilienceLevel']]

print(df)
resilience_counts = df['ResilienceLevel'].value_counts()
print(resilience_counts)
