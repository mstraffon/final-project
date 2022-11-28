'''
Jessica Shaffer

This visualization is a scatterplot that displays the correlation between danceability and valence of top songs in the 2010s.
'''

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
import seaborn as sb
import statsmodels.api as sm

def danceval():
    df = pd.read_csv('top10s.csv', header = 0, encoding="ISO-8859-1")

    df = df.drop(df.index[[50, 138, 267, 362, 442]])
    df = df.reset_index()

    x = df['val']
    y = df['dnce']

    sb.regplot(x, y, ci=None, color = 'black')

    plt.scatter(x, y, color = 'mediumseagreen')

    plt.ylabel('Danceability', fontsize=20, labelpad=10)
    plt.xlabel('Valence', fontsize=20, labelpad = 10)

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))

    plt.title('Valence vs Danceability of Top Songs in the 2010s', fontsize=24, pad=20)

    plt.show()

def main():
    danceval()


if __name__ == '__main__':
    main()
