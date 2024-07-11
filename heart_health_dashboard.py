import streamlit as st
import requests

st.title("Heart Stroke Prediction")

age = st.slider("Age", 0, 100)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", [0, 1])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.slider("Average Glucose Level", 0.0, 200.0)
bmi = st.slider("BMI", 0.0, 50.0)
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

if st.button("Predict"):
    response = requests.post("http://localhost:8005/predict", json={
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "ever_married": ever_married,
        "work_type": work_type,
        "Residence_type": Residence_type,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "smoking_status": smoking_status
    })

    if response.status_code == 200:
        st.write("Stroke Probability:", response.json()["stroke_probability"])
    else:
        st.write("Error:", response.text)