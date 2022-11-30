'''
megan straffon
image 2'''
#imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read csv
df=pd.read_csv("spotify_top50_2021.csv",usecols=['energy','popularity'],nrows=50)

#make graph
plt.xlabel('Energy Level (0-1)',fontsize=20)
plt.ylabel("Popularity Score (1-100)",fontsize=20)
plt.title("Are Popular Songs More Energetic?",fontsize=20)

plt.scatter(df.energy,df.popularity,color="mediumseagreen",edgecolor="black")
z=np.polyfit(df.energy, df.popularity,0)
p=np.poly1d(z)
plt.plot(df.energy, p(df.popularity),color='black')
plt.show()
