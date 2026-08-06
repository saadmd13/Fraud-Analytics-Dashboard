import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import traceback

# =====================================================
# PostgreSQL Configuration
# =====================================================

DB_USER = "postgres"
DB_PASSWORD = "saad"          # <-- Your PostgreSQL password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fraud_analytics"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

# =====================================================
# Load Dataset
# =====================================================

print("=" * 60)
print("FRAUD ANALYTICS ETL PIPELINE")
print("=" * 60)

print("\nReading cleaned dataset...")

df = pd.read_csv("data/processed/cleaned_creditcard.csv")

print(f"Dataset Shape : {df.shape}")
print(f"Columns       : {len(df.columns)}")

print("\nColumn Names:")
print(df.columns.tolist())

# =====================================================
# Rename Target Column
# =====================================================

if "Class" in df.columns:
    df.columns = df.columns.str.lower()
    df.rename(columns={"class": "actual_class"}, inplace=True)
    print("\nUpdated Column Names:")
    print(df.columns.tolist())

# =====================================================
# Upload Dataset
# =====================================================

try:

    print("\nUploading transactions to PostgreSQL...")

    df.to_sql(
        name="transactions",
        con=engine,
        if_exists="append",
        index=False,
        chunksize=1000      # Smaller chunks make debugging easier
    )

    print("\nUpload Successful!")

    with engine.connect() as conn:

        result = conn.execute(
            text("SELECT COUNT(*) FROM transactions")
        )

        total_rows = result.scalar()

        print(f"\nRows in Database : {total_rows}")

except Exception as e:

    print("\n" + "=" * 60)
    print("DATABASE ERROR")
    print("=" * 60)

    print(type(e).__name__)
    print(e)

    print("\nFull Error:")
    traceback.print_exc()