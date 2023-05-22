import pandas as pd
import numpy as np



def main():
    df = pd.read_csv('data.csv', low_memory=False)
    col = "popularity"
    
    
    df_train = df[(df['year'] > 1979) & (df['year'] < 2000)]
    df_train = df_train.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_train_x = df_train.loc[:, df_train.columns != col]
    np.savetxt("trainx2.csv", df_train_x, delimiter=",")
    df_train_y = df_train[[col]].copy()
    np.savetxt("trainy2.csv", df_train_y, delimiter=",")
    
    
    
    df_test = df[df['year'] == 2000]
    df_test = df_test.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_test.to_csv("test.csv")
    df_test_x = df_test.loc[:, df_test.columns != col]
    np.savetxt("testx2.csv", df_test_x, delimiter=",")
    df_test_y = df_test[[col]].copy()
    np.savetxt("testy2.csv", df_test_y, delimiter=",")









main()