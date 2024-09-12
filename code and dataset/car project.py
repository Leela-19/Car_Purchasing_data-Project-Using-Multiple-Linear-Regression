'''
In this file we are going to develop and Multiple Linear Regression with Oops concept
'''
import numpy as np
import pandas as pd
import sklearn
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


class TRAIN:
    def __init__(self, file):
        try:
            self.data = pd.read_csv(file, encoding='latin1')
            # self.print(data)
            self.data = self.data.drop(['Customer Name', 'Customer e-mail', 'Country'], axis=1)
            # print(self.data)
            self.X = self.data.iloc[:, :-1]
            self.y = self.data.iloc[:, -1]
            # print(self.X)
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2,
                                                                                    random_state=2)
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

    def TRAINING(self):
        try:
            self.reg = LinearRegression()
            self.reg.fit(self.X_train, self.y_train)
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

    def TRAINED_PERFORMANCE(self):
        try:
            self.y_train_pred = self.reg.predict(self.X_train)
            print(f'Train Accuracy : {r2_score(self.y_train, self.y_train_pred)}')
            print(f'Train Loss using Mean_Squared_Error : {mean_squared_error(self.y_train, self.y_train_pred)}')
            print(f'Train Loss Using absolute mean error : {mean_absolute_error(self.y_train, self.y_train_pred)}')
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

    def TESTING(self):
        try:
            self.reg = LinearRegression()
            self.reg.fit(self.X_test, self.y_test)
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')

    def TEST_PERFORMANCE(self):
        try:
            self.y_test_pred = self.reg.predict(self.X_test)
            print(f'Test Accuracy : {r2_score(self.y_test, self.y_test_pred)}')
            print(f'Test Loss using Mean_Squared_Error : {mean_squared_error(self.y_test, self.y_test_pred)}')
            print(f'Test Loss Using absolute mean error : {mean_absolute_error(self.y_test, self.y_test_pred)}')
        except Exception as e:
            error_type, error_msg, err_line = sys.exc_info()
            print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')


if __name__ == "__main__":
    try:
        sri = TRAIN('C:\\Users\\leela\\Downloads\\ML\\pythonProject\\Car_Purchasing_Data.csv')
        sri.TRAINING()
        sri.TRAINED_PERFORMANCE()
        sri.TESTING()
        sri.TEST_PERFORMANCE()
    except Exception as e:
        error_type, error_msg, err_line = sys.exc_info()
        print(f'Error from Line {err_line.tb_lineno} -> type {error_type} -> Error msg -> {error_msg}')
