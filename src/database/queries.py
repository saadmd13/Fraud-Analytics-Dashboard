from sqlalchemy import text
from src.database.connection import engine

# =====================================================
# Dashboard Summary
# =====================================================

def get_dashboard_summary():

    with engine.connect() as conn:

        total_transactions = conn.execute(
            text("SELECT COUNT(*) FROM transactions")
        ).scalar()

        fraud_cases = conn.execute(
            text("""
                SELECT COUNT(*)
                FROM transactions
                WHERE actual_class = 1
            """)
        ).scalar()

        legitimate_cases = conn.execute(
            text("""
                SELECT COUNT(*)
                FROM transactions
                WHERE actual_class = 0
            """)
        ).scalar()

        fraud_percentage = round(
            (fraud_cases / total_transactions) * 100,
            4
        )

        return {
            "total_transactions": total_transactions,
            "fraud_cases": fraud_cases,
            "legitimate_cases": legitimate_cases,
            "fraud_percentage": fraud_percentage,
        }

# =====================================================
# Get Recent Transactions
# =====================================================

def get_transactions(limit=100):

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT *
                FROM transactions
                ORDER BY transaction_id
                LIMIT :limit
            """),
            {"limit": limit}
        )

        rows = result.fetchall()

        return [dict(row._mapping) for row in rows]

# =====================================================
# Get Single Transaction
# =====================================================

def get_transaction(transaction_id):

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT *
                FROM transactions
                WHERE transaction_id = :id
            """),
            {"id": transaction_id}
        )

        row = result.fetchone()

        if row:
            return dict(row._mapping)

        return None

# =====================================================
# Fraud Transactions
# =====================================================

def get_fraud_transactions(limit=100):

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT *
                FROM transactions
                WHERE actual_class = 1
                ORDER BY amount DESC
                LIMIT :limit
            """),
            {"limit": limit}
        )

        rows = result.fetchall()

        return [dict(row._mapping) for row in rows]

# =====================================================
# Random Legitimate Transaction
# =====================================================

def get_random_legitimate():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT *
                FROM transactions
                WHERE actual_class = 0
                ORDER BY RANDOM()
                LIMIT 1
            """)
        )

        row = result.fetchone()

        if row:
            return dict(row._mapping)

        return None

# =====================================================
# Random Fraud Transaction
# =====================================================

def get_random_fraud():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT *
                FROM transactions
                WHERE actual_class = 1
                ORDER BY RANDOM()
                LIMIT 1
            """)
        )

        row = result.fetchone()

        if row:
            return dict(row._mapping)

        return None