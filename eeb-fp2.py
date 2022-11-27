import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Reading data from CSV
df = pd.read_csv('spotify_top50_2021.csv', usecols=[4,5,6,8,14])

# Data manipulation
r = df['valence'].corr(df['loudness'])
print(r**2)
plt.plot('valence', 'loudness', data=df, linestyle='none', marker='o')
plt.show()