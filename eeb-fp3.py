import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Reading data from CSV
df = pd.read_csv('spotify_top50_2021.csv', usecols=[0,5])

# Plotting
plt.figure('Image 3')
plt.hist(df['danceability'], bins=10, edgecolor='black')

plt.title("Danceability of the Top 50 Streamed Songs (2021)", fontsize=16)
plt.xlabel('Danceability Score', fontsize=13)
plt.ylabel('# of songs', fontsize=13)
plt.show()