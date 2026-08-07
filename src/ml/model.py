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
        transaction.time,
        transaction.v1,
        transaction.v2,
        transaction.v3,
        transaction.v4,
        transaction.v5,
        transaction.v6,
        transaction.v7,
        transaction.v8,
        transaction.v9,
        transaction.v10,
        transaction.v11,
        transaction.v12,
        transaction.v13,
        transaction.v14,
        transaction.v15,
        transaction.v16,
        transaction.v17,
        transaction.v18,
        transaction.v19,
        transaction.v20,
        transaction.v21,
        transaction.v22,
        transaction.v23,
        transaction.v24,
        transaction.v25,
        transaction.v26,
        transaction.v27,
        transaction.v28,
        transaction.amount,
    ]

    # Convert to NumPy array
    features = np.array(features).reshape(1, -1)

    # Apply the same scaler used during training
    features_scaled = scaler.transform(features)

    # Predict class
    prediction = model.predict(features_scaled)[0]

    # Predict fraud probability
    probability = model.predict_proba(features_scaled)[0][1]

    return {
        "prediction": int(prediction),
        "label": "Fraud" if prediction == 1 else "Legitimate",
        "fraud_probability": round(float(probability), 4),
    }