'''
megan straffon
image 2'''
#imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("globalchart2.csv",usecols=['rank','artist_names','track_name','weeks_on_chart','streams'],nrows=5)
print(df)

plt.xlabel('Artists',fontsize=20)
plt.ylabel("Number of Streams in 10millions",fontsize=20)
plt.title("Spotify Top Chart 11/17/22 Top Artists",fontsize=20)
plt.bar(df.artist_names,df.streams,color='mediumseagreen',edgecolor="black")
plt.show()

