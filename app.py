from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model safely
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        garage = float(request.form['garage'])
        age = float(request.form['age'])

        features = np.array([[area, bedrooms, bathrooms, garage, age]])
        prediction = model.predict(features)

        result = f"Predicted Price: ${int(prediction[0])}"

    except Exception as e:
        result = "Invalid Input!"

    return render_template('index.html', prediction_text=result)

# 🔥 IMPORTANT FOR DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
