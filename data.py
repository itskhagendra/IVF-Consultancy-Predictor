# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# data Processing
import pandas
from numpy import array, ravel

filename = 'dataset.txt'
names = ["season", "age", "childish", "accident", "Surgical", "Fever History", "Alcohol", "smoking", "Idle", "Output"]
raw_data = pandas.read_csv(filename, names=names)
x_data, y_data = raw_data.iloc[:, :9], raw_data.iloc[:, 9:]
x_train, x_test = x_data[:85], x_data[85:]
y_train, y_test = y_data[:85], y_data[85:]

# Data Processing
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

classifier = SVC()
encoder = LabelEncoder()
y_test, y_train = array(y_train), array(y_test)
y_train = ravel(y_train)
y_test = ravel(y_test)
y_test, y_train = encoder.fit_transform(y_train), encoder.fit_transform(y_test)

# AI Traoining
classifier.fit(x_train, y_train)
pred = classifier.predict(x_test)
acc = accuracy_score(pred, y_test)
print(acc)

# Production Ready
import pickle

model = pickle.dump(classifier, open('model1.h5', 'wb'))
production = pickle.load(open('model1.h5', 'rb'))

# print("1.Winter")
# print("2.Spring")
# print("3.Summer")
# print("4.fall")
# print("Enter The choice of season")
# se=int(input())
# =============================================================================
# s={'winter':-1,'Spring':-0.33,'Summer':0.33,'fall':1}
# =============================================================================
# season=s[se]

#Figures
import matplotlib.pyplot as plt
#plt.scatter(x_train[['Alcohol']],x_train[['Idle']])



x = array([-0.33, 0.67, 0, 1, 1, 0, 0.8, 1, .31])
x = x.reshape(1, -1)
print(production.predict(x))
