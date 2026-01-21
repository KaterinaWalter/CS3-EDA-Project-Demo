import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud 
from collections import Counter

# Load & View Data
df_colors = pd.read_csv('MTA_Colors.csv')

# Format a series (column) from the dataframe to use
service_series = df_colors['Service']
service_list = service_series.values
services = Counter(service_list)

# Create a wordcloud from that data
wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(services)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  
plt.title("Word Cloud")
plt.savefig('wordcloud.png', bbox_inches='tight')
