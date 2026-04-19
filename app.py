from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

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

    except:
        result = "Invalid Input!"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)