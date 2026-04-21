'''
This will contain code that uses the model stored in the folder "model" to
perform a prediction
'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from wf_ml_training import Linear_Regression
import sklearn



if __name__ == '__main__':
    df = pd.read_csv("data_original/human_selected_dataset.csv")
    df_binary = df[['code_size', 'label']]

    X = np.array(df_binary['code_size']).reshape(-1, 1)
    Y = np.array(df_binary['label']).reshape(-1, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)
    regression = Linear_Regression()
    print(regression.predict(X_test))