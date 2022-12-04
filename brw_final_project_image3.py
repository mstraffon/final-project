'''
Briley Winge Final Project 
Image 3 
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
df = artist
mean_tracks = artist['tracks'].describe()

print(mean_tracks)

artist = artist[artist['tracks'] > 192] 

artist = artist.reset_index(drop=True)

x = artist['one_billion']
y = artist['feats']

plt.figure(figsize=(17, 10))
sns.boxplot( x= x, y= y, width = 0.7, linewidth = 3, palette="Greens")
plt.xlabel("Number of Tracks That Reached One Billion Streams", fontsize = 12)
plt.ylabel("Number of Streams Artist/Band is Featured On", fontsize = 12)
plt.title("Number of One Billion Records vs Number of Streams for Featured Tracks",y=1,fontsize=14,color = 'mediumseagreen',fontweight='bold')

plt.show()