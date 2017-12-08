from sklearn.preprocessing import Imputer
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, cross_val_predict
from sklearn import datasets
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import sklearn
import numpy as np
import pandas as pd
import datetime as date

# Preprocessing Dataset
dataframe = pd.read_csv("./data/scraped_events.csv", delimiter=',')

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    dataframe['What'].values,
    dataframe['Where'].values,
    dataframe['When'].values,
    dataframe['How_Much'].values,
    test_size=0.2, random_state=5)

linear_regr = linear_model.LinearRegression()

# Train the model on the training data using linear regression model
linear_regr.fit(x_train.reshape(-1,1), y_train.reshape(-1,1))
predict_regr = linear_regr.predict(x_test.reshape(-1,1))

coefficient_variable = linear_regr.coef_
intercept_variable = linear_regr.intercept_


def kfold_cross_validation():

    x = dataframe[dataframe].values.reshape(-1, len(vars))
    y = dataframe['Kfold']

    logistic_regr = linear_model.LogisticRegression()

    kf = KFold(n_splits=10)

    calculated_list = []

    for train_index, test_index in kf.split(x, y):
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]

        logistic_regr.fit(x_train, y_train)

    predict_regr = cross_val_predict(logistic_regr, x_test, y_test, cv=10)


print("test")


def run():

    print("Coefficient: ", coefficient_variable)
    print("Intercept: ", intercept_variable)

        
run()