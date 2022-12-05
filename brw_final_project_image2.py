'''
Briley Winge Final Project
Image 2 
'''

import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import pandas as pd
import math
import seaborn as sns
from matplotlib import lines
from matplotlib import patches
from matplotlib.patheffects import withStroke


artist = pd.read_csv('spotify_artist_data.csv', index_col = 0, header = 0)

artist = artist.drop(index =[101])
artist = artist.drop(index =[202])
artist = artist.drop(index =[303])
artist = artist.drop(index =[404])
artist = artist.drop(index =[505])
artist = artist.drop(index =[606])
artist = artist.drop(index =[707])
artist = artist.drop(index =[808])
artist = artist.drop(index =[909])

artist.columns = ['artist_name', 'lead_streams', 'feats', 'tracks', 'one_billion', '100_million', 'last_updated']

artist = artist.reset_index(drop=True)

artist['lead_streams'] = artist['lead_streams'].str.replace(",","").astype(float)
artist = artist.astype({'lead_streams':'int'})

artist['feats'] = artist['feats'].str.replace(",","").astype(float)
artist = artist.astype({'feats':'int'})

artist['tracks'] = artist['tracks'].str.replace(",","").astype(float)
artist = artist.astype({'tracks':'int'})

artist = artist.astype({'one_billion':'int'})
artist = artist.astype({'100_million':'int'})

artist = artist[artist['one_billion'] > 0] 

artist = artist[artist['100_million'] > 0] 

artist = artist.reset_index(drop=True)

mean_tracks = artist['tracks'].describe()

print(mean_tracks)

artist = artist[artist['tracks'] > 192] 

artist = artist.reset_index(drop=True)

mean_tracks = artist['100_million'].describe()

print(mean_tracks)

artist = artist[artist['100_million'] > 27] 
artist = artist.reset_index(drop=True)

height = artist['100_million']
bars = artist['artist_name']
y_pos = np.arange(len(bars))

plt.bar(y_pos, height, color= 'mediumseagreen')

plt.xticks(y_pos, bars)

plt.gca().set_xticks(plt.gca().get_xticks()[::4])
plt.xlabel("Artist Name", fontsize = 14)
plt.ylabel("Number of Tracks That Reached 100 Million Streams", fontsize = 10)
plt.title("Number of One Million Tracks Per Each Artist/Band",y=1,fontsize=12,color = 'mediumseagreen', fontweight='bold')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
