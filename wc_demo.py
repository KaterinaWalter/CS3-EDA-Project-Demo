import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set_theme(style="ticks", palette="pastel")

# Load & View Data
df_colors = pd.read_csv('MTA_Colors.csv')

print(df_colors.info())

# *** WORD CLOUD ***

# format a series (column) from the dataframe to use
wc_series = df_colors['Service']
print(wc_series)
service_list = str(wc_series.values)
print(service_list)
service_str = ' '.join(item for item in service_list.split())
print(service_str)

# .generate takes in a STRING like:
sample_str = "penne fusilli rigatoni gnocchi spaghetti farfalle linguini bucatini lasagna stelline"

# Create a wordcloud from that data
wordcloud = WordCloud(width=800, height=400).generate(service_str)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.title("Word Cloud")
plt.savefig('wordcloud.png', bbox_inches='tight')
