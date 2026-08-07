from fastapi import FastAPI, HTTPException

from src.api.schemas import Transaction
from src.database.queries import (
    get_dashboard_summary,
    get_transactions,
    get_transaction,
    get_fraud_transactions,
    get_random_legitimate,
    get_random_fraud,
)
from src.ml.model import predict_transaction

# =====================================================
# FastAPI Application
# =====================================================

app = FastAPI(
    title="Fraud Analytics API",
    description="Backend API for Fraud Analytics Dashboard",
    version="1.0.0",
)

# =====================================================
# Home
# =====================================================

@app.get("/")
def home():

    return {
        "message": "Fraud Analytics API is Running!"
    }


# =====================================================
# Dashboard Summary
# =====================================================

@app.get("/dashboard")
def dashboard():

    return get_dashboard_summary()


# =====================================================
# Transactions
# =====================================================

@app.get("/transactions")
def transactions(limit: int = 100):

    return get_transactions(limit)


# =====================================================
# Single Transaction
# =====================================================

@app.get("/transactions/{transaction_id}")
def transaction(transaction_id: int):

    data = get_transaction(transaction_id)

    if data is None:

        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return data


# =====================================================
# Fraud Transactions
# =====================================================

@app.get("/fraud-transactions")
def fraud_transactions(limit: int = 100):

    return get_fraud_transactions(limit)


# =====================================================
# Fraud Prediction
# =====================================================

@app.post("/predict")
def predict(transaction: Transaction):

    return predict_transaction(transaction)

# =====================================================
# Random Legitimate Transaction
# =====================================================

@app.get("/random-legitimate")
def random_legitimate():

    return get_random_legitimate()


# =====================================================
# Random Fraud Transaction
# =====================================================

@app.get("/random-fraud")
def random_fraud():

    return get_random_fraud()