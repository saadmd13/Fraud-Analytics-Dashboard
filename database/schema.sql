-- =========================================================
-- Fraud Analytics Dashboard Database Schema
-- =========================================================

-- Drop tables if they already exist
DROP TABLE IF EXISTS predictions;
DROP TABLE IF EXISTS model_metrics;
DROP TABLE IF EXISTS transactions;

-- =========================================================
-- Transactions Table
-- =========================================================

CREATE TABLE transactions (

    transaction_id SERIAL PRIMARY KEY,

    time INTEGER NOT NULL,

    v1 DOUBLE PRECISION,
    v2 DOUBLE PRECISION,
    v3 DOUBLE PRECISION,
    v4 DOUBLE PRECISION,
    v5 DOUBLE PRECISION,
    v6 DOUBLE PRECISION,
    v7 DOUBLE PRECISION,
    v8 DOUBLE PRECISION,
    v9 DOUBLE PRECISION,
    v10 DOUBLE PRECISION,
    v11 DOUBLE PRECISION,
    v12 DOUBLE PRECISION,
    v13 DOUBLE PRECISION,
    v14 DOUBLE PRECISION,
    v15 DOUBLE PRECISION,
    v16 DOUBLE PRECISION,
    v17 DOUBLE PRECISION,
    v18 DOUBLE PRECISION,
    v19 DOUBLE PRECISION,
    v20 DOUBLE PRECISION,
    v21 DOUBLE PRECISION,
    v22 DOUBLE PRECISION,
    v23 DOUBLE PRECISION,
    v24 DOUBLE PRECISION,
    v25 DOUBLE PRECISION,
    v26 DOUBLE PRECISION,
    v27 DOUBLE PRECISION,
    v28 DOUBLE PRECISION,

    amount DOUBLE PRECISION,

    actual_class INTEGER NOT NULL
);

-- =========================================================
-- Predictions Table
-- =========================================================

CREATE TABLE predictions (

    prediction_id SERIAL PRIMARY KEY,

    transaction_id INTEGER REFERENCES transactions(transaction_id),

    prediction INTEGER,

    probability DOUBLE PRECISION,

    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    model_version VARCHAR(50)
);

-- =========================================================
-- Model Metrics Table
-- =========================================================

CREATE TABLE model_metrics (

    metric_id SERIAL PRIMARY KEY,

    model_name VARCHAR(100),

    accuracy DOUBLE PRECISION,

    precision_score DOUBLE PRECISION,

    recall DOUBLE PRECISION,

    f1_score DOUBLE PRECISION,

    roc_auc DOUBLE PRECISION,

    trained_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);