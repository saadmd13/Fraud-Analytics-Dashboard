from sqlalchemy import create_engine, text

# =====================================================
# PostgreSQL Configuration
# =====================================================

DB_USER = "postgres"
DB_PASSWORD = "saad"          # Your PostgreSQL password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fraud_analytics"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


# =====================================================
# Total Transactions
# =====================================================

def get_total_transactions():

    with engine.connect() as conn:

        result = conn.execute(
            text("SELECT COUNT(*) FROM transactions")
        )

        return result.scalar()


# =====================================================
# Total Fraud Cases
# =====================================================

def get_total_fraud_cases():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT COUNT(*)
                FROM transactions
                WHERE actual_class = 1
            """)
        )

        return result.scalar()


# =====================================================
# Total Legitimate Cases
# =====================================================

def get_total_legitimate_cases():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT COUNT(*)
                FROM transactions
                WHERE actual_class = 0
            """)
        )

        return result.scalar()


# =====================================================
# Fraud Percentage
# =====================================================

def get_fraud_percentage():

    fraud = get_total_fraud_cases()
    total = get_total_transactions()

    return round((fraud / total) * 100, 4)


# =====================================================
# Amount Statistics
# =====================================================

def get_amount_statistics():

    with engine.connect() as conn:

        result = conn.execute(
            text("""
                SELECT
                    MIN(amount),
                    MAX(amount),
                    AVG(amount)
                FROM transactions
            """)
        )

        return result.fetchone()


if __name__ == "__main__":

    print("=" * 50)

    print("Database Summary")

    print("=" * 50)

    print("Total Transactions :", get_total_transactions())

    print("Fraud Cases        :", get_total_fraud_cases())

    print("Legitimate Cases   :", get_total_legitimate_cases())

    print("Fraud Percentage   :", get_fraud_percentage(), "%")

    stats = get_amount_statistics()

    print("\nAmount Statistics")

    print("-------------------------")

    print("Minimum :", round(stats[0], 2))

    print("Maximum :", round(stats[1], 2))

    print("Average :", round(stats[2], 2))

    