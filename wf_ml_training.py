'''
 This will contain code that constructs one (or more) models from your data.
Executing it will save file(s) which stores the model(s).
'''
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression


#Resource that I used as a 'tutorial': https://www.geeksforgeeks.org/machine-learning/python-linear-regression-using-sklearn/
def regression():
    df = pd.read_csv("data_original\\human_selected_dataset.csv")
    df_binary = df[['code_size', 'label']]

    X = np.array(df_binary['code_size']).reshape(1,-1)
    Y = np.array(df_binary['label']).reshape(1,-1)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20, train_size=0.80)

    regr_model = LinearRegression()
    regr_model.fit(X_train, y_train)
    print(regr_model.score(X_test, y_test))

    return regr_model



#NOTE: used this as a resource for helping understand how to use sklearn's KNClassifier
#https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn
def knn_sklearn(y_train, y_test, x_train, x_test, k = 4, tests=30):

    knn = KNeighborsClassifier(n_neighbors=4)
    knn.fit(x_train, y_train)
    predicted_y = knn.predict(x_test)
    acc = accuracy_score(y_test, predicted_y)

    print("Sklearn Accuracy: ", acc * 100, "%")



if __name__ == '__main__':

    file = pd.read_csv('data_processed\\training_set.csv')
    x_train, y_train = file['code_size'], file['label']

    file = pd.read_csv('data_processed\\testing_set.csv')
    x_test, y_test = file['code_size'], file['label']

    x_train = np.array(x_train)
    x_test = np.array(x_test)

    x_train = x_train.reshape(-1, 3804)
    x_test = x_test.reshape(-1, 951)


    #UNCOMMENT THE MODELS NOT CURRENTLY RUNNING!

    #knn_sklearn(y_train, y_test, x_train, x_test)
    regression()
