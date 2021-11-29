from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    features_name = ['step', 'type', 'amount','oldbalanceOrig','newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
    df = pd.DataFrame(features_value, columns = features_name)
    output = model.predict(df)

    if output ==1:
        res_val= "true"
    else:
        res_val = "false"

    return render_template('index.html',pred='The fraudulent activity is {}'.format(res_val))

if __name__ == '__main__':
    app.run(debug=True)