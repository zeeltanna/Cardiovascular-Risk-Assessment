# -*- coding: utf-8 -*-

import os
import numpy as np
import pickle
from flask import Flask, request, render_template

# Define the directory where your model is stored
model_directory = "C:/Users/zeelt/Desktop/Python Projects/Major Project/My Project"
model_file = "model.pkl"

# Construct the full file path using os.path.join
model_path = os.path.join(model_directory, model_file)

# Load ML model
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('Heart_Disease_Classifier.html')

# Bind predict function to URL
@app.route('/predict', methods=['POST'])
def predict():
    # Get form entries as list
    features = [float(i) for i in request.form.values()]
    # Convert features to numpy array
    array_features = np.array(features).reshape(1, -1)
    # Predict
    prediction = model.predict(array_features)
    
    output = prediction[0]  # Extract the prediction from numpy array
    
    # Determine result message based on prediction
    if output == 1:
        result = 'The patient is likely to have heart disease!'
    else:
        result = 'The patient is not likely to have heart disease!'
    
    # Pass result to HTML template
    return render_template('Heart_Disease_Classifier.html', result=result)

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
