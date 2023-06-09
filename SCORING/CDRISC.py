import pandas as pd
from pathlib import Path 

def resilience_score(row):
    score = 0
    for i in range(1, 26):
        score += row[f'V2IA{i:02}']
    return score

def resilience_level(score):
    if score < 50:
        return 'Low Resilience'
    elif score < 75:
        return 'Moderate Resilience'
    else:
        return 'High Resilience'

def main():
    csv4 = Path('V2I.CSV')  
    dfd = pd.read_csv(csv4)

    dfd['TotalResilienceScore'] = dfd.apply(resilience_score, axis=1)
    dfd['ResilienceLevel'] = dfd['TotalResilienceScore'].apply(resilience_level)

    dfd = dfd[['PublicID', 'TotalResilienceScore', 'ResilienceLevel']]
    
    print(dfd)
    dfd.to_csv('Resilience.csv', index=False)

main()