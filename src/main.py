# main program 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_corr(df, size=11):

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)   # color code the rectangles by correlation value
    plt.xticks(range(len(corr.columns)), corr.columns)  # draw x tick marks
    plt.yticks(range(len(corr.columns)), corr.columns)  # draw y tick marks
    plt.show()

def main():
    df = pd.read_csv('./data/pima-data.csv')
    print(df.isnull().values.any())
    # ensure  no correlated values
    # checks the values on the plot
    plot_corr(df)



if __name__ == "__main__":
    main()


#
