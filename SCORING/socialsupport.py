import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path 

csv_file = Path(__file__).with_name('V2I.CSV')  # Load the CSV file
df = pd.read_csv(csv_file)  # Read the CSV into a DataFrame

def compute_resilience_score(row):
    total_score = row[['V2IA{:02d}'.format(i) for i in range(1, 26)]].sum()
    
    return pd.Series({
        'TotalScore': total_score, #give distribution of this 
    })

def resilience_level(score):
    if score <= 50:
        return 'Low Resilience'
    elif score <= 75:
        return 'Moderate Resilience'
    else:
        return 'High Resilience'

df = df.join(df.apply(compute_resilience_score, axis=1))
df['ResilienceLevel'] = df['TotalScore'].apply(resilience_level)

# Select only the necessary columns
df = df[['PublicID', 'TotalScore', 'ResilienceLevel']]

# Get counts of individuals in each resilience level
resilience_counts = df['ResilienceLevel'].value_counts()
print(resilience_counts)

# Plot histogram of total score
plt.hist(df['TotalScore'], bins='auto')
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.title('Distribution of Total Score')
plt.show()

print(df)
 # dont make cut off not informative