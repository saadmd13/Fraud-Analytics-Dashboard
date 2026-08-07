import streamlit as st
import pandas as pd
import plotly.express as px

from api import (
    get_dashboard,
    get_transactions,
    get_fraud_transactions,
    get_transaction,
)

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Fraud Analytics Dashboard",
    page_icon="💳",
    layout="wide",
)

# =====================================================
# Sidebar
# =====================================================

st.sidebar.title("💳 Fraud Analytics")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Transactions",
        "Prediction"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Backend Connected ✅")

# =====================================================
# DASHBOARD PAGE
# =====================================================

if page == "Dashboard":

    st.title("💳 Fraud Analytics Dashboard")

    # -----------------------------
    # Load Data
    # -----------------------------

    summary = get_dashboard()

    transactions = pd.DataFrame(
        get_transactions(limit=10000)
    )

    # -----------------------------
    # KPI Cards
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Transactions",
            f"{summary['total_transactions']:,}"
        )

    with col2:
        st.metric(
            "Fraud Cases",
            f"{summary['fraud_cases']:,}"
        )

    with col3:
        st.metric(
            "Legitimate Transactions",
            f"{summary['legitimate_cases']:,}"
        )

    with col4:
        st.metric(
            "Fraud Percentage",
            f"{summary['fraud_percentage']}%"
        )

    st.divider()

    # =====================================================
    # Charts
    # =====================================================

    chart1, chart2 = st.columns(2)

    # -----------------------------
    # Fraud Distribution
    # -----------------------------

    with chart1:

        st.subheader("Fraud Distribution")

        fraud_counts = (
            transactions["actual_class"]
            .map({
                0: "Legitimate",
                1: "Fraud"
            })
            .value_counts()
            .reset_index()
        )

        fraud_counts.columns = [
            "Class",
            "Count"
        ]

        fig = px.pie(
            fraud_counts,
            names="Class",
            values="Count",
            hole=0.45,
            title="Fraud vs Legitimate",
            color="Class",
            color_discrete_map={
                "Legitimate": "#2ECC71",
                "Fraud": "#E74C3C",
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -----------------------------
    # Amount Histogram
    # -----------------------------

    with chart2:

        st.subheader(
            "Transaction Amount Distribution"
        )

        fig = px.histogram(
            transactions,
            x="amount",
            nbins=50,
            title="Transaction Amount Distribution"
        )

        fig.update_layout(
            xaxis_title="Amount ($)",
            yaxis_title="Number of Transactions"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # =====================================================
    # Fraud Scatter Plot
    # =====================================================

    st.subheader("Fraud Transactions Over Time")

    fraud = transactions[
        transactions["actual_class"] == 1
    ]

    if len(fraud) > 0:

        fig = px.scatter(
            fraud,
            x="time",
            y="amount",
            color="amount",
            title="Fraud Transactions",
            color_continuous_scale="Reds"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No fraud transactions available in the loaded sample."
        )

    st.divider()

    # =====================================================
    # Top 20 Largest Transactions
    # =====================================================

    st.subheader("💰 Top 20 Largest Transactions")

    top_transactions = (
        transactions
        .sort_values(
            "amount",
            ascending=False
        )
        .head(20)
    )

    st.dataframe(
        top_transactions,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # Download CSV
    # =====================================================

    st.download_button(
        label="⬇ Download Transactions CSV",
        data=transactions.to_csv(index=False),
        file_name="transactions.csv",
        mime="text/csv"
    )

# =====================================================
# TRANSACTIONS PAGE
# =====================================================

elif page == "Transactions":

    st.title("📋 Transaction Explorer")

    st.markdown("Search, filter and explore transaction records.")

    st.divider()

    col1, col2 = st.columns([3, 1])

    with col1:

        transaction_id = st.number_input(
            "Search Transaction ID",
            min_value=1,
            step=1
        )

    with col2:

        fraud_only = st.checkbox("Fraud Only")

    st.divider()

    if fraud_only:

        transactions = pd.DataFrame(
            get_fraud_transactions(limit=500)
        )

    else:

        transactions = pd.DataFrame(
            get_transactions(limit=1000)
        )

    # Search Result

    if transaction_id > 0:

        transaction = get_transaction(transaction_id)

        if isinstance(transaction, dict):

            st.subheader("Transaction Details")

            st.json(transaction)

        else:

            st.error("Transaction not found.")

    st.subheader("Transactions")

    st.dataframe(
        transactions,
        use_container_width=True,
        height=500
    )

    st.download_button(
        "⬇ Download CSV",
        transactions.to_csv(index=False),
        "transactions.csv",
        "text/csv"
    )

# =====================================================
# PREDICTION PAGE
# =====================================================

elif page == "Prediction":

    st.title("🤖 Fraud Prediction")

    st.info(
        "Prediction form will be added in the next step."
    )