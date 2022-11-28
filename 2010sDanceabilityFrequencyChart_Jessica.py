'''
Jessica Shaffer

This visualization is a bar chart that displays the frequency of danceability measurements of top songs in the 2010s.
'''

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
import seaborn as sb
import statsmodels.api as sm

def frequency():
    df = pd.read_csv('top10s.csv', header = 0, encoding="ISO-8859-1")
    s = pd.Series(df['dnce']).value_counts().sort_index()
    s

    s = s.reindex(range(22, 99), fill_value=0)
    s.tail()
    ax = s.plot.bar()
    ax2 = ax.twinx()
    s2 = s / sum(s)
    s2.plot.bar(ax=ax2, color='mediumseagreen')

    ax2.set_ylabel('Estimated Probability', fontsize=18, labelpad = 20)
    ax.set_ylabel('Frequency', fontsize=18, labelpad = 20)
    for label in ax.xaxis.get_ticklabels()[1::2]:
        label.set_visible(False)

    ax.set_xlabel('Danceability', fontsize = 18, labelpad = 10)

    plt.title('Frequency of Danceability Measurements of Top Songs in the 2010s', fontsize=24, pad = 20)
    plt.show()

def main():
    frequency()


if __name__ == '__main__':
    main()
