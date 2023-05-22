import numpy as np
from matplotlib import pyplot as plt
from statistics import mean


def main():
    X_train = np.loadtxt('trainx2.csv', delimiter=',')
    y_train = np.loadtxt('trainy2.csv', delimiter=',')
    
    X_test = np.loadtxt('testx2.csv', delimiter=',')
    y_test = np.loadtxt('testy2.csv', delimiter=',')
    
    
    
    alpha_1 = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train.T
    print(alpha_1)
    print()
    
    differences = []
    for z in range(X_test.shape[0]):
        # print(y_test[z])
        # print(sum(X_test[z] * alpha_1))
        a = y_test[z]
        b = sum(X_test[z] * alpha_1)
        diff = abs(a-b)
        differences.append(diff)
        
    print(mean(differences))
        
    sorted_differences = np.sort(differences)
    p = 1. * np.arange(len(sorted_differences)) / float(len(sorted_differences) - 1)

    plt.plot(sorted_differences, p)
    plt.xlabel('Abs_Diff(Pred-Obs popularity)')
    plt.ylabel('Proportion of Difference')
    plt.title('D=13, Train=2000-2019, Test=2020, CDF graph')
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