import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for STACKED BAR CHART
df_clothes = pd.DataFrame({'Season': ['Fall', 'Fall', 'Fall', 'Spring', 'Spring', 'Spring', 'Spring'],
                   'Item': ['Tops', 'Skirts', 'Skirts', 'Tops', 'Skirts', 'Dresses', 'Dresses'],
                   'Amount': [50, 60, 100, 75, 30, 90, 30]
                   })

# Pivot data to prepare for stacked bar chart
pivot_df = df_clothes.pivot_table(index='Season', columns='Item', values='Amount', aggfunc='sum', fill_value=0)

# Create stacked bar chart
pivot_df.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Clothing Items by Season')
plt.xlabel('Season')
plt.ylabel('Amount')
plt.legend(title='Item')
plt.savefig('stacked_bar_clothes.png', bbox_inches='tight')

# Sample data
df_crime = pd.DataFrame({'State': ['NY', 'NY', 'NY', 'CA', 'CA', 'CA', 'CA', 'TX', 'TX'],
                         'City': ['New York', 'Buffalo', 'Ithaca', 'Los Angeles', 'Sacramento', 'San Francisco', 'San Diego', 'Houston', 'Dallas'],
                         'Crime_Rate': [5.2, 6.3, 7.1, 4.8, 9.0, 8.5, 7.2, 3.4, 4.1]
                        })

# Pivot data to prepare for stacked bar chart
pivot_df_crime = df_crime.pivot_table(index='State', columns='City', values='Crime_Rate', aggfunc='sum', fill_value=0)

# Create stacked bar chart
pivot_df_crime.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Crime Rate by State and City (Stacked Bars)')
plt.xlabel('State')     
plt.ylabel('Crime Rate')
plt.legend(title='City')
plt.savefig('stacked_bar_crime.png', bbox_inches='tight')
plt.close()

# Create catplot -> grouped bars with cities side by side for each state
sns.catplot(x='State', y='Crime_Rate', hue='City', data=df_crime, kind='bar', height=6, aspect=1.5)
plt.title('Crime Rate by State and City (Grouped Bars)')
plt.savefig('catplot_crime.png', bbox_inches='tight')
plt.close()