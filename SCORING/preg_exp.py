import pandas as pd
from pathlib import Path 

csv_file = Path(__file__).with_name('V3J.CSV')  # Load the CSV file
df = pd.read_csv(csv_file)  # Read the CSV into a DataFrame

# Define scoring function
def compute_scores(row):
    uplifts_frequency = sum(row['V3JA01a':'V3JA01j'] > 0)
    hassles_frequency = sum(row['V3JA02a':'V3JA02j'] > 0)
    uplifts_intensity = row['V3JA01a':'V3JA01j'].sum() / uplifts_frequency if uplifts_frequency > 0 else 0
    hassles_intensity = row['V3JA02a':'V3JA02j'].sum() / hassles_frequency if hassles_frequency > 0 else 0
    hassle_uplift_frequency_ratio = hassles_frequency / uplifts_frequency if uplifts_frequency > 0 else 0
    hassle_uplift_intensity_ratio = hassles_intensity / uplifts_intensity if uplifts_intensity > 0 else 0
    
    return pd.Series({
        'FrequencyOfHassles': hassles_frequency,
        'FrequencyOfUplifts': uplifts_frequency,
        'IntensityOfHassles': hassles_intensity,
        'IntensityOfUplifts': uplifts_intensity,
        'HassleUpliftFrequencyRatio': hassle_uplift_frequency_ratio,
        'HassleUpliftIntensityRatio': hassle_uplift_intensity_ratio
    })

# Apply scoring function to compute scores
df = df.join(df.apply(compute_scores, axis=1))

# Select only the necessary columns
df = df[['PublicID', 'FrequencyOfHassles', 'FrequencyOfUplifts', 'IntensityOfHassles', 
         'IntensityOfUplifts', 'HassleUpliftFrequencyRatio', 'HassleUpliftIntensityRatio']]

print(df)
