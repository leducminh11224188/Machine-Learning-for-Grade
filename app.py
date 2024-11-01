# app.py
from flask import Flask, request, jsonify
import pandas as pd
import pickle
import sklearn

app = Flask(__name__)

# Load mô hình
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

with open('weather_classifier.pkl', 'rb') as f:
    weather_model = pickle.load(f)

# Route để dự đoán AQI
@app.route('/predict_temperature', methods=['POST'])
def predict_temperature():
    data = request.get_json()
    input_data = pd.DataFrame(data)
    prediction = rf_model.predict(input_data)
    prediction_rounded = [round(value) for value in prediction]
    return jsonify({'Temperature_prediction': prediction_rounded})


# Route để dự đoán kiểu thời tiết
@app.route('/predict_weather', methods=['POST'])
def predict_weather():
    data = request.get_json()
    input_data = pd.DataFrame(data)
    prediction = weather_model.predict(input_data)
    return jsonify({'Weather_prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
