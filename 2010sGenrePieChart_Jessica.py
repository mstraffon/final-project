'''
Jessica Shaffer

This visualization is a pie chart of the top 10 genres from top 50 world song charts from each year of the 2010s.
'''

import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import pandas as pd
import seaborn as sb
import statsmodels.api as sm

def pie():
    df = pd.read_csv('top10s.csv', header = 0, encoding="ISO-8859-1")

    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    df['top genre'].value_counts().head(10).plot.pie(figsize=(15,10), autopct='%0.0f%%', fontsize = 7, explode = explode, labeldistance = 1.05)
    plt.title('Top Genres in the 2010s', fontsize = 24, pad = 10)

    plt.axis('off')

    plt.show()

def main():
    pie()


if __name__ == '__main__':
    main()