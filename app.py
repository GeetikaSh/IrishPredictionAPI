from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

# Crearing App
app = FastAPI(title="Irish SVM Prediction API")

# Load Model
model = joblib.load("pipeline/svm_irish_pipeline.pkl")

# Input Schema
class InputFeatures(BaseModel):
    SepalLengthCm: float = Field(..., description="Sepal length in cm (e.g., 5.1)")
    SepalWidthCm: float = Field(..., description="Sepal width in cm (e.g., 3.5)")
    PetalLengthCm: float = Field(..., description="Petal length in cm (e.g., 1.4)")
    PetalWidthCm: float = Field(..., description="Petal width in cm (e.g., 0.2)")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris SVM Classifier API!"}

@app.post("/predict/")
def predict_species(data: InputFeatures):
    features = np.array([[data.SepalLengthCm, data.SepalWidthCm, data.PetalLengthCm, data.PetalWidthCm]])
    prediction = model.predict(features)
    return {"predicted_label": int(prediction[0])}
