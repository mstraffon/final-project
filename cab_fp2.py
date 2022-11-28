#Final Project Visualizations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#First is a histogram
df = pd.read_csv('spotify_artist_data.csv', index_col=0, 
    header=0)
print(df)
for row in range(1,6):
    val= df.loc[row, 'lead_streams']
    val = val.replace(',','')
    print(val)
    df.loc[row, 'lead_streams'] = int(val)
    print(type(df.loc[row, 'lead_streams']))

x = ['Drake', 'Bad Bunny', 'Ed Sheeran', 'The Weeknd', 'Taylor Swift']
y = df['lead_streams']
print(y)
plt.ylabel('Streams (Billions)', fontsize=15).set_color('black')
plt.title(label='Top Five Spotify Artists Lead Streams')
plt.bar(x,y.head(), color='mediumseagreen', edgecolor='darkgreen')
plt.show()
