import numpy as np
import math
import csv

import pandas as pd
from pandas.core.methods.selectn import DataFrame
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.linear_model import ElasticNet
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

from wf_ml_training import knn_sklearn
from wf_ml_training import Linear_Regression


'''
 This will contain code that splits your data into test and training sets (which
be stored in the "models" folder), trains a model (by calling functions in wf_training.py), and then
evaluates it by performing prediction on the test set (by calling functions in wf_prediction.py). This
le provides a secondary entry point to running your work ow. It should be assumed that wf_core.py
has previously executed to populate the data_processed folder.
'''

def data_splitter():
    file = open("data_original/human_selected_dataset.csv", encoding="utf-8", mode = "r")
    datafile = csv.reader(file)
    total_records = sum(1 for row in datafile)

    file = open("data_original/human_selected_dataset.csv", encoding="utf-8", mode = "r")
    datafile = csv.reader(file)

    test_count = math.ceil(0.20 * total_records)
    train_count = math.floor(0.80 * total_records)

    print("test count: ", test_count)
    print("train_count ", train_count)

    test_set = list()
    train_set = list()
    count = 0



    for entry in datafile:
        # print("entry ", count, ": ", entry)
        # print("count: ", count)
        if count <= train_count:
            train_set.append(entry)

        else:
            test_set.append(entry)


        count += 1

    file = open('data_processed/testing_set.csv', encoding="utf-8", mode='w', newline='')
    writer = csv.writer(file)
    writer.writerow(["submission_id", "problem_id", "user_id", "date", "language", "original_language", "filename_ext", "status", "cpu_time", "memory", "code_size", "accuracy", "status_in_folder", "code", "label", "LLM"])
    writer.writerows(test_set)

    file = open('data_processed/training_set.csv', encoding="utf-8", mode='w', newline='')
    writer = csv.writer(file)
    # writer.writerow(["problem_id", "submission_id", "LLM", "status_in_folder", "code", "label"])
    writer.writerows(train_set)
    print("total records: ", count)


# used example on scikit-learn.org as base
def ElasticNet_regression():
    df = pd.read_csv("data_original\\human_selected_dataset.csv")
    df_binary = df[['code_size', 'label']]

    X = np.array(df_binary['code_size']).reshape(1,-1)
    Y = np.array(df_binary['label']).reshape(1,-1)

    # X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20, train_size=0.80)

    x, y = make_regression(n_features=2, random_state=0)

    regr_model = ElasticNet(random_state=0)
    regr_model.fit(X, Y)
    # print(regr_model.score(X_test, y_test))

    return regr_model

# used example on scikit-learn.org as base
def LASSO_regression():
    X, Y = make_regression(n_features=2, random_state=0)

    lasso = linear_model.Lasso(alpha=0.5,copy_X=X)
    lasso.fit([[0,0], [1,1], [2,2], [0, 1, 2]])

    return lasso

#source used as tutorial: https://data36.com/polynomial-regression-python-scikit-learn/
def polynomial_regression():
    df = pd.read_csv("data_original\\human_selected_dataset.csv")
    df_binary = df[['code_size', 'label']]

    X = np.array(df_binary['code_size']).reshape(1,-1)
    Y = np.array(df_binary['label']).reshape(1,-1)

    regression = PolynomialFeatures(degree=2, include_bias=True)
    poly = regression.fit_transform(X.reshape(-1,1))

    reg_model = Linear_Regression()
    reg_model.fit(poly, Y)

    y_predict = reg_model.predict(poly)

    return reg_model


def stat_eval():

    file = open('Models\\evaluation\\summary.txt', 'w')

    file.write("Baseline System: \n")

    data = {
        "Dataset": ["human_selected_dataset"],
        "Method": ["K-Nearest Neighbor"],
        "Accuracy": [0.0],
        "Precision": [0.0]
    }
    df = pd.DataFrame(data)
    file.write(df.to_string())

    file.write('\n')
    file.write('\n')
    file.write('\n')


    file.write("Actual System: \n")
    data2 = {
        "Dataset": ["human_selected_dataset"],
        "Method": ["Linear Regression"],
        "Accuracy": [0.0],
        "Precision": [0.0]
    }
    df2 = pd.DataFrame(data2)
    file.write(df2.to_string())

    file.close()

if __name__ == '__main__':
    data_splitter()
    stat_eval()
    polynomial_regression()
    LASSO_regression()
    ElasticNet_regression()