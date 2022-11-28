import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('songs.csv', index_col=0, header=0)

print(df.head())

df['danceability'] = df['danceability'].astype(float)
df = df.astype({'danceability':'float'})
height = df['danceability'].head()
print(height)
bars = df['song_title'].head()
print(bars)

plt.figure(figsize=(10,8))
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color='orchid', edgecolor='darkmagenta')
plt.xticks(y_pos, bars)
plt.xlabel("Song Title", fontsize = 16)
plt.ylabel("Danceability", fontsize = 14)
plt.title("Five Songs and Their Danceability" ,y=1,fontsize=16,fontweight='bold')

plt.show()
