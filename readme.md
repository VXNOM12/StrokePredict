## 💖 Heart Stroke Prediction App

### 📋 Description
A simple app to predict the likelihood of a heart stroke based on various health factors. Stay ahead of your health with this easy-to-use tool!

### 📦 Installation
To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

### 🚀 Usage
To run the app, use the following command:

```bash
streamlit run heart_health_dashboard.py
```

### 🌐 API Endpoint
The API endpoint is available at `/predict`. You can send a POST request with the following JSON payload:

```json
{
    "age": int,
    "hypertension": int,
    "heart_disease": int,
    "ever_married": int,
    "work_type": str,
    "Residence_type": str,
    "avg_glucose_level": float,
    "bmi": float,
    "smoking_status": str
}
```

### 📊 Model Performance
The model has an accuracy of **0.87** and the following classification report:

```plaintext
              precision    recall  f1-score   support

           0       0.94      0.92      0.93       960
           1       0.10      0.15      0.12        62

    accuracy                           0.87      1022
   macro avg       0.52      0.53      0.52      1022
weighted avg       0.89      0.87      0.88      1022
```

### 🔢 Confusion Matrix
```plaintext
[[880  80]
 [ 53   9]]
```

### 🛠️ Requirements
The following packages are required to run the app:

```plaintext
altair==4.0.0
fastapi==0.70.0
imblearn==0.8.0
pydantic==1.9.0
scikit-learn==1.0.2
streamlit==1.10.0
```

### 👤 Author
VXNOM12

---
