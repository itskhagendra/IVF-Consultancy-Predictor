# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:44:46 2018

@author: Khagendra
"""

from flask import Flask, render_template, jsonify, request
import pickle

app = Flask(__name__)
production = pickle.load(open('model1.h5', 'rb'))


def res(x):
    x = x.reshape(1, -1)
    return production.predict(x)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api")
def api():
    result = {'Name': "Khagendra Kumar", 'Reg': 'RA1511003040044'}
    return jsonify(result)


if __name__ == '__main__':
    app.run()
