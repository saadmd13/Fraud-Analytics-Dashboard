from fastapi import FastAPI
from src.database.queries import get_dashboard_summary

from src.api.schemas import Transaction
from src.ml.model import predict_transaction

app = FastAPI(
    title="Fraud Analytics API",
    description="Backend API for Fraud Analytics Dashboard",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Fraud Analytics API is Running!"
    }


@app.get("/dashboard")
def dashboard():

    return get_dashboard_summary()

from fastapi import HTTPException

from src.database.queries import (
    get_dashboard_summary,
    get_transactions,
    get_transaction,
    get_fraud_transactions,
)
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

    result = predict_transaction(transaction)

    return result