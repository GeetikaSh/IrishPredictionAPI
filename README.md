# Iris Species Prediction API using FastAPI

The min purpose of this project was to built an API on **FastAPI** to classify the Irish Species, which serves predictions using the pre-trained **Support Vector Machine (SVM)** model.

[Link of Kaggle Notebook for trained model and data](https://www.kaggle.com/code/sharmageetika/iris-prediction-with-fast-api?scriptVersionId=243951941)

---

## Features
- RESTful API built using FastAPI
- Trained on the Iris dataset using SVM
- Accepts real-time input for sepal and petal measurements
- Pre-trained model serialized with `joblib`
- **Predicts Iris species label (`0`, `1`, or `2`)**

---
## To Do
- Map Predicted Iris Species Labels '1', '2', '3' to the original Iris Species Labels.

---

## Project Structure
|--app.py #FastAPI application
|--svm_irish_pipeline.pkl #Pre-trained SVM model
|--requirements.txt # Python dependencies
|--README.md # Project documentation
|--streamlit webapp
