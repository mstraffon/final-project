'''
megan straffon
image 1'''
#imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#reading csv into file
df=pd.read_csv("data.csv",usecols=['danceability','duration_ms'],nrows=700)

#changing duration to int so i can change it to minutes
df['duration_ms'] = df['duration_ms'].astype(int)

#change duration to minutes
df.duration_ms/=(1000*60)
#change scale from 0-1 to 0-10
df.danceability*=10

#making plot!
plt.xlabel('Song Length(mins)',fontsize=20)
plt.ylabel("Danceability scale(1-10)",fontsize=20)
plt.title("Danceability vs Song Length",fontsize=20)
plt.scatter(df.duration_ms,df.danceability,color='mediumseagreen',edgecolors="darkslategray")
z=np.polyfit(df.duration_ms, df.danceability, 1)
p=np.poly1d(z)
plt.plot(df.duration_ms, p(df.duration_ms),color='black')


plt.show()



