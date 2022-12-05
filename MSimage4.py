'''
megan straffon
image 2'''
#imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read csv
df=pd.read_csv("songs_normalize.csv",usecols=['popularity','energy'],na_values=['0','1','2','3'])


print(df.corr(method='pearson'))


#make graph
plt.xlabel('Popularity Score (1-100)',fontsize=20)
plt.ylabel("Energy Level (0-1)",fontsize=20)
plt.title("Are Popular Songs More Energetic? Pt.2",fontsize=20)

plt.scatter(df.popularity,df.energy,color="mediumseagreen",edgecolor="black")
z=np.polyfit(df.popularity, df.energy,0)
p=np.poly1d(z)
plt.plot(df.popularity, p(df.energy),color='black')
plt.show()

