from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pandas as pd
from joblib import load
import json
import logging

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)

def load_model():
    try:
        return load('model/titanic_model_rf.pkl')
    except:
        logging.error('Model not loaded')

model = load_model()

def predict_new(X, probs=True):
    p = model.get_preprocessing()
    
    X = p.clean_data(X)
    X = p.categ_encoding(X)
    
    columns = model.get_columns()
    for col in columns:
        if col not in X.columns:
            X[col] = 0
    if probs:
        return model.predict_proba(X)[:,1]
    else:
        return model.predict(X)


@app.route('/invocations', methods=['POST'])
def predict():
    data = pd.read_json(request.json)
    predictions = np.array2string(predict_new(data, probs=True))
    return jsonify(predictions)

@app.route('/health', methods=['GET'])
def health_check():
    resp = jsonify(success=True)
    return resp


if __name__ == "__main__":
    model = load_model()
    app.run(debug=True, host='0.0.0.0', port=5000)
