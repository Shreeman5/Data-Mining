import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np







def main():
    df = pd.read_csv('data.csv', low_memory=False)
    col = "popularity"
    
    
    df_train = df[(df['year'] > 1959) & (df['year'] < 1980)]
    df_train = df_train.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_train_x = df_train.loc[:, df_train.columns != col]
    # df_train_x.to_csv("train.csv")
    # x = StandardScaler().fit_transform(df_train_x)
    np.savetxt("trainx2.csv", df_train_x, delimiter=",")
    df_train_y = df_train[[col]].copy()
    # y = StandardScaler().fit_transform(df_train_y)
    np.savetxt("trainy2.csv", df_train_y, delimiter=",")
    
    
    
    df_test = df[df['year'] == 1980]
    df_test = df_test.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_test_x = df_test.loc[:, df_test.columns != col]
    # x_1 = StandardScaler().fit_transform(df_test_x)
    np.savetxt("testx2.csv", df_test_x, delimiter=",")
    df_test_y = df_test[[col]].copy()
    # y_1 = StandardScaler().fit_transform(df_test_y)
    np.savetxt("testy2.csv", df_test_y, delimiter=",")









main()