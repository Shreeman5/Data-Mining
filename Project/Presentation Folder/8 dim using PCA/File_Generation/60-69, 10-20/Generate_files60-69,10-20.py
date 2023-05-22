import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np


def main():
    df = pd.read_csv('data.csv', low_memory=False)
    col = "popularity"
    
    
    df_train = df[((df['year'] > 1959) & (df['year'] < 1970)) | ((df['year'] > 2009) & (df['year'] < 2020))]
    df_train = df_train.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_train_x = df_train.loc[:, df_train.columns != col]
    x = StandardScaler().fit_transform(df_train_x)
    pca = PCA(n_components=8)
    principalComponents = pca.fit_transform(x)
    np.savetxt("trainx2.csv", principalComponents, delimiter=",")
    df_train_y = df_train[[col]].copy()
    np.savetxt("trainy2.csv", df_train_y, delimiter=",")
    
    df_test = df[df['year'] == 2020]
    df_test = df_test.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_test_x = df_test.loc[:, df_test.columns != col]
    x_1 = StandardScaler().fit_transform(df_test_x)
    pca_1 = PCA(n_components=8)
    principalComponents_1 = pca_1.fit_transform(x_1)
    np.savetxt("testx2.csv", principalComponents_1, delimiter=",")
    df_test_y = df_test[[col]].copy()
    np.savetxt("testy2.csv", df_test_y, delimiter=",")
    
    

    

    


main()
