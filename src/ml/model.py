import joblib
import numpy as np
from pathlib import Path

# =====================================================
# Load Model & Scaler
# =====================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "models" / "fraud_detection_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# =====================================================
# Prediction Function
# =====================================================

def predict_transaction(transaction):

    # Create feature vector in the SAME order used during training
    features = [
        transaction.Time,
        transaction.V1,
        transaction.V2,
        transaction.V3,
        transaction.V4,
        transaction.V5,
        transaction.V6,
        transaction.V7,
        transaction.V8,
        transaction.V9,
        transaction.V10,
        transaction.V11,
        transaction.V12,
        transaction.V13,
        transaction.V14,
        transaction.V15,
        transaction.V16,
        transaction.V17,
        transaction.V18,
        transaction.V19,
        transaction.V20,
        transaction.V21,
        transaction.V22,
        transaction.V23,
        transaction.V24,
        transaction.V25,
        transaction.V26,
        transaction.V27,
        transaction.V28,
        transaction.Amount,
    ]

    # Convert to NumPy array
    features = np.array(features).reshape(1, -1)

    # Apply the same scaler used during training
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)[0]

    # Probability of fraud (Class = 1)
    probability = model.predict_proba(features_scaled)[0][1]

    # Return prediction
    return {
        "prediction": int(prediction),
        "label": "Fraud" if prediction == 1 else "Legitimate",
        "fraud_probability": float(probability)
    }