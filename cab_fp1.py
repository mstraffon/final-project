import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('spotify_artist_data.csv', index_col=0, header=0)

df['onehundred_million'] = df['onehundred_million'].astype(float)
df = df.astype({'onehundred_million':'int'})

df['Tracks'] = df['Tracks'].astype(float)
df = df.astype({'Tracks':'int'})

x = df['onehundred_million']
y = df['Tracks']

sns.regplot(x=df['onehundred_million'], y=df['Tracks'], scatter_kws={"color": "mediumseagreen"}, line_kws={"color": "darkgreen"})
plt.xlabel("Number of Tracks That Reached 100 Million", fontsize = 16)
plt.ylabel("Number of Tracks Artist Has Released", fontsize = 14)
plt.title("Number of 100 Million Records Dependent" +'\n'+ "on Number of Tracks",y=1,fontsize=16,fontweight='bold')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
