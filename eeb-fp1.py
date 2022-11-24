import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Reading data from CSV
df = pd.read_csv('spotify_top50_2021.csv', usecols=[1,4,5,6])

# Data manipulation
num_hits = df['artist_name'].value_counts()
top_6_num_hits = num_hits.iloc[0:6]
y_pos = np.arange(6)

# Plotting
plt.figure('Image 1', figsize=(10,5))
plt.bar(y_pos, top_6_num_hits.values)
plt.xticks(y_pos, top_6_num_hits.index)
plt.yticks(np.arange(5))

plt.title("Artists with the Most Songs in the Top 50 (2021)")
plt.xlabel('Artist')
plt.ylabel('# of songs in Top 50 Streamed Songs')
plt.show()