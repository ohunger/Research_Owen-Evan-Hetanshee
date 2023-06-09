import pandas as pd
from pathlib import Path 

csv_file = Path(__file__).with_name('V2A.CSV')  # Load the CSV file
df = pd.read_csv(csv_file)  # Read the CSV into a DataFrame

'''
• Purpose: Captures respondents’ experience with unfair treatment in their daily lives
• NuMom2b: Utilizes the 9 item Daily Discrimination scale (Self-administered)
• Response options: Respondents complete the Daily Discrimination Scale by indicating
how often they feel discriminate against on a 1 to 4 scale
o 1 = often
o 2 = sometime
o 3 = rarely
o 4 = never
• Scoring:
o All items reverse scored
o Sum all items
▪ higher scores mean more frequent experiences of discrimination.
• Variables: Visit 2: V2AG01 - V2AG03i
'''