from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
    age: int
    hypertension: int
    heart_disease: int
    ever_married: int
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str

@app.post("/predict")
async def predict_stroke(request: PredictionRequest):
    input_data = [
        request.age,
        request.hypertension,
        request.heart_disease,
        request.ever_married,
        request.work_type,
        request.Residence_type,
        request.avg_glucose_level,
        request.bmi,
        request.smoking_status
    ]

    prediction = model.predict([input_data])
    return {"stroke_probability": prediction[0]}