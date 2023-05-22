import pandas as pd
import numpy as np




def main():
    df = pd.read_csv('data.csv', low_memory=False)
    col = "popularity"
    
    
    df_train = df[(df['year'] > 1999) & (df['year'] < 2020)]
    df_train = df_train.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_train_x = df_train.loc[:, df_train.columns != col]
    np.savetxt("trainx2.csv", df_train_x, delimiter=",")
    df_train_y = df_train[[col]].copy()
    np.savetxt("trainy2.csv", df_train_y, delimiter=",")
    
    
    
    df_relevant = df[df['year'] == 2020]
    
    
    df_test_popular = df_relevant[(df_relevant['artists'].str.contains('Drake')) | 
                                    (df_relevant['artists'].str.contains('Justin Bieber')) |
                                    (df_relevant['artists'].str.contains('Dua Lipa'))] 
    df_test_popular = df_test_popular.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_test_popular.to_csv("popular.csv")
    df_test_popular_x = df_test_popular.loc[:, df_test_popular.columns != col]
    np.savetxt("testx2_popular.csv", df_test_popular_x, delimiter=",")
    df_test_popular_y = df_test_popular[[col]].copy()
    np.savetxt("testy2_popular.csv", df_test_popular_y, delimiter=",")
    
    
    df_test_unpopular = df_relevant[(df_relevant['artists'].str.contains('Rauw Alejandro')) | 
                                    (df_relevant['artists'].str.contains('Sech')) |
                                    (df_relevant['artists'].str.contains('Tones And I')) |
                                    (df_relevant['artists'].str.contains('Lauv')) | 
                                    (df_relevant['artists'].str.contains('Ali Gatie')) |
                                    (df_relevant['artists'].str.contains('Zoe Wees')) |
                                    (df_relevant['artists'].str.contains('Little Mix')) | 
                                    (df_relevant['artists'].str.contains('Lee Brice'))] 
    df_test_unpopular = df_test_unpopular.drop(['artists', 'id', 'name', 'year', 'release_date'], axis=1)
    df_test_unpopular.to_csv("unpopular.csv")
    df_test_unpopular_x = df_test_unpopular.loc[:, df_test_unpopular.columns != col]
    np.savetxt("testx2_unpopular.csv", df_test_unpopular_x, delimiter=",")
    df_test_unpopular_y = df_test_unpopular[[col]].copy()
    np.savetxt("testy2_unpopular.csv", df_test_unpopular_y, delimiter=",")
    
    



# | (df_relevant['artists'] == 'Bad Bunny') | 
#                                 (df_relevant['artists'] == 'Lil Uzi Vert')
#                        | (df_relevant['artists'] == 'Dua Lipa') | (df_relevant['artists'] == 'Twenty One Pilots')





main()