import requests

BASE_URL = "http://127.0.0.1:8000"


# =====================================================
# Dashboard
# =====================================================

def get_dashboard():
    return requests.get(f"{BASE_URL}/dashboard").json()


# =====================================================
# Transactions
# =====================================================

def get_transactions(limit=1000):
    return requests.get(
        f"{BASE_URL}/transactions?limit={limit}"
    ).json()


def get_transaction(transaction_id):
    return requests.get(
        f"{BASE_URL}/transactions/{transaction_id}"
    ).json()


def get_fraud_transactions(limit=100):
    return requests.get(
        f"{BASE_URL}/fraud-transactions?limit={limit}"
    ).json()


# =====================================================
# Random Transactions
# =====================================================

def get_random_legitimate():
    return requests.get(
        f"{BASE_URL}/random-legitimate"
    ).json()


def get_random_fraud():
    return requests.get(
        f"{BASE_URL}/random-fraud"
    ).json()


# =====================================================
# Prediction
# =====================================================

def predict(transaction):

    return requests.post(
        f"{BASE_URL}/predict",
        json=transaction
    ).json()