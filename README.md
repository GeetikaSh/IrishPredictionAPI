# Iris Species Prediction API using FastAPI

The min purpose of this project was to built an API on **FastAPI** to classify the Irish Species, which serves predictions using the pre-trained **Support Vector Machine (SVM)** model.

[Link of Kaggle Notebook for trained model and data](https://www.kaggle.com/code/sharmageetika/iris-prediction-with-fast-api?scriptVersionId=243951941)

---

## Features
- RESTful API built using FastAPI
- Trained on the Iris dataset using SVM
- Accepts real-time input for sepal and petal measurements
- Pre-trained model serialized with `joblib`
- **Predicts Iris species label     0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'**

---

## Project Structure
├── app.py # FastAPI application serving prediction API\
├── streamlit_app.py # Streamlit frontend application\
├── pipeline/\
│ └── svm_irish_pipeline.pkl # Pre-trained ML model pipeline\
├── requirements.txt # Python dependencies\
├── Dockerfile # Docker configuration to build combined app container\
└── README.md # This file

## Running with Docker (Recommended)

### Build Docker Image
```bash
docker build --no-cache -t iris-combined .
```
### Run Docker Container
```bash
docker run -p 8000:8000 -p 8501:8501 iris-combined
```
