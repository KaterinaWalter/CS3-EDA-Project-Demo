import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
df = pd.DataFrame({'Season': ['Fall', 'Fall', 'Fall', 'Spring', 'Spring', 'Spring', 'Spring'],
                   'Item': ['Tops', 'Skirts', 'Skirts', 'Tops', 'Skirts', 'Dresses', 'Dresses'],
                   'Amount': [50, 60, 100, 75, 30, 90, 30]
                   })
print(df.info())
print(df['Season'].value_counts()) # number of rows for each season
print(df.groupby('Season')['Amount'].sum()) # total amount for each season
