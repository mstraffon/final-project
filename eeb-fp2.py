import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
# valence is the independent variable!

# Reading data from CSV
df = pd.read_csv('spotify_top50_2021.csv', usecols=[4,5,6,8,14])

# Linear regression work
m, b = np.polyfit(df['valence'], df['loudness'], deg=1)
xs = np.linspace(0, 1, num=50)
model = sm.OLS(df['loudness'], df['valence'])
results= model.fit()
print("R squared:" , results.rsquared)

# Plotting
plt.figure('Image 2')
plt.plot('valence', 'loudness', data=df, linestyle='none', marker='o', color="mediumseagreen")
plt.plot(xs, m*xs + b, lw=3, color="darkgreen")
plt.title("Valence vs. Loudness (Top 50 Songs 2021)", fontsize=18)
plt.xlabel('Valence (1 = more positive mood)', fontsize=14)
plt.ylabel('Loudness (higher value = louder)', fontsize=14)
plt.show()