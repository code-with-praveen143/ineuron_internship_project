import numpy as np
from flask import Flask, render_template, request, redirect, url_for
import pickle
import re
import pandas as pd
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    password_list = []
    password_list.append(username)
    password_list.append(password)
    my_data = pd.DataFrame(password_list)
    passwords = my_data.to_csv('passwords.csv')
    if (username in password_list) and (password in password_list):
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 1)

    return render_template('index.html', prediction_text='Your Rating is: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
