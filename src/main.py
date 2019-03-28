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

    # deletes the column that it is consider correlated to another
    del df['skin']

    # modilg data
    diabetes_map = {True: 1, False: 0}
    df['diabetes'] = df['diabetes'].map(diabetes_map)

    # checks rare events see if there is enough values to make the prediction check true/false ratio
    num_obs = len(df)
    num_true = len(df.loc[df['diabetes'] == 1])
    num_false = len(df.loc[df['diabetes'] == 0])
    print("Number of True cases:  {0} ({1:2.2f}%)".format(num_true, (num_true/num_obs) * 100))
    print("Number of False cases: {0} ({1:2.2f}%)".format(num_false, (num_false/num_obs) * 100))




if __name__ == "__main__":
    main()


#
