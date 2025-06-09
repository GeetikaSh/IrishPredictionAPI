# streamlit_app.py

import streamlit as st
import requests

# App Title
st.title("🌸 Iris Species Predictor (via FastAPI)")
st.write("Enter the flower's measurements:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1, value=0.2)

# API URL - Update if hosted elsewhere
API_URL = "http://localhost:8000/predict/"

# Predict
if st.button("Predict"):
    payload = {
        "SepalLengthCm": sepal_length,
        "SepalWidthCm": sepal_width,
        "PetalLengthCm": petal_length,
        "PetalWidthCm": petal_width
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🌼 Predicted Species: **{result['predicted_label']}**")
        else:
            st.error(f"Prediction failed. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error calling API: {e}")