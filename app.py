from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

# Creating App
app = FastAPI(title="Iris SVM Prediction API")

# Load Model
model = joblib.load("pipeline/svm_irish_pipeline.pkl")

# Input Schema
class InputFeatures(BaseModel):
    SepalLengthCm: float = Field(..., description="Sepal length in cm (e.g., 5.1)")
    SepalWidthCm: float = Field(..., description="Sepal width in cm (e.g., 3.5)")
    PetalLengthCm: float = Field(..., description="Petal length in cm (e.g., 1.4)")
    PetalWidthCm: float = Field(..., description="Petal width in cm (e.g., 0.2)")

# Label Mapping
iris_labels = {
    0: 'Iris-setosa',
    1: 'Iris-versicolor',
    2: 'Iris-virginica'
}

@app.get("/")
def read_root():
    """
    Root route for sanity check.
    """
    return {"message": "Welcome to the Iris SVM Classifier API!"}

@app.post("/predict/")
def predict_species(data: InputFeatures):
    """
    Predict the Iris species from flower features.
    """
    features = np.array([[data.SepalLengthCm, data.SepalWidthCm,
                          data.PetalLengthCm, data.PetalWidthCm]])
    prediction = model.predict(features)[0]
    label = iris_labels.get(int(prediction), "Unknown")

    return {
        "predicted_label": label,
        "prediction_code": int(prediction)
    }