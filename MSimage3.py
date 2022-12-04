'''
megan straffon
image 3'''
#imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read csv
df=pd.read_csv("spotify_top50_2021.csv",usecols=['energy','popularity'])


#make graph
plt.xlabel('Popularity Score (1-100)',fontsize=20)
plt.ylabel("Energy Level (0-1)",fontsize=20)
plt.title("Are Popular Songs More Energetic?",fontsize=20)

plt.scatter(df.popularity,df.energy,color="mediumseagreen",edgecolor="black")
z=np.polyfit(df.popularity, df.energy,0)
p=np.poly1d(z)
plt.plot(df.popularity, p(df.energy),color='black')
plt.show()
