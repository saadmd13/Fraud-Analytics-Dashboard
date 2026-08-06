from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# ==========================================
# PostgreSQL Configuration
# ==========================================

DB_USER = "postgres"
DB_PASSWORD = "saad"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "fraud_analytics"

# ==========================================
# Database URL
# ==========================================

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================
# Create Engine
# ==========================================

engine = create_engine(DATABASE_URL)

# ==========================================
# Test Connection
# ==========================================

try:
    connection = engine.connect()
    print("✅ Connected to PostgreSQL Successfully!")
    connection.close()

except SQLAlchemyError as e:
    print("❌ Connection Failed")
    print(e)