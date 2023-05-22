import numpy as np
from matplotlib import pyplot as plt
from statistics import mean


def main():
    X_train = np.loadtxt('trainx2.csv', delimiter=',')
    y_train = np.loadtxt('trainy2.csv', delimiter=',')
    
    X_test = np.loadtxt('testx2.csv', delimiter=',')
    y_test = np.loadtxt('testy2.csv', delimiter=',')
    
    
    
    alpha_1 = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train.T
    
    differences = []
    for z in range(X_test.shape[0]):
        a = y_test[z]
        b = sum(X_test[z] * alpha_1)
        diff = abs(a-b)
        differences.append(diff)
        
    print(mean(differences))
        
    plt.hist(differences, bins = 10)
 
    plt.title('D=2 using PCA, Train=1960-60, 2010-19, Test=2020')
    plt.xlabel('Absolute Difference Between Predicted and Actual Value')
    plt.ylabel('Frequency of absolute difference')
 
    # show plot
    plt.show()
    
    
    
    # print(len(alpha_1))
    # print(alpha_1)
    # error_y_1 = np.linalg.norm(y_test-X_test@alpha_1, 2)
    # print(error_y_1)
    
    
    # s = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
    # for x in range(len(s)):
    #     alpha_2 = np.linalg.inv(X_train.T @ X_train + s[x] * np.identity(13)) @ X_train.T @ y_train.T
    #     print(alpha_2)
    #     error_y_2 = np.linalg.norm(y_test-X_test@alpha_2, 2)
    #     print('RRError:', error_y_2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()