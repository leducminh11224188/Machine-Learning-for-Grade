# app_ui.py
import streamlit as st
import requests
import pandas as pd

st.title("Weather Prediction")

# Input cho dự đoán nhiệt độ
st.header("Weather Prediction")
temperature = st.number_input("Apparent Temperature (C)", value=32)
humidity = st.number_input("Humidity", value=0.61)
wind_bearing = st.number_input("Wind Bearing (degrees)", value=85)
visibility = st.number_input("Visibility (km)", value=24)

# Button gửi yêu cầu đến API
if st.button("Predict Temperature"):
    data = {'Apparent Temperature (C)': [temperature], 'Humidity': [humidity],
            'Wind Bearing (degrees)': [wind_bearing], 'Visibility (km)': [visibility]}
    response = requests.post('http://127.0.0.1:5000/predict_temperature', json=data)
    temperature = response.json()['Temperature_prediction'][0]
    st.write(f"Predicted Temperature: {temperature}")

# Input cho dự đoán thời tiết
st.header("Weather Prediction")
temperature = st.number_input("Temperature (C)", value=31)
apparent_temperature = st.number_input("Apparent Temperature (C)", value=33)
humidity = st.number_input("Humidity", value=0.59)
wind_speed = st.number_input("Wind Speed (km/h)", value=3)
pressure = st.number_input("Pressure (millibars)", value=1007)

if st.button("Predict Weather"):
    data = {'Temperature (C)': [temperature], 'Apparent Temperature (C)': [apparent_temperature],
            'Humidity': [humidity], 'Wind Speed (km/h)': [wind_speed],
            'Wind Bearing (degrees)': [wind_bearing], 'Visibility (km)': [visibility],
            'Loud Cover': [0], 'Pressure (millibars)': [pressure]}
    response = requests.post('http://127.0.0.1:5000/predict_weather', json=data)
    weather = response.json()['Weather_prediction'][0]
    st.write(f"Predicted Weather: {weather}")
