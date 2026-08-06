import streamlit as st
import pandas as pd
import plotly.express as px

from api import (
    get_dashboard,
    get_transactions,
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
# Dashboard Title
# =====================================================

st.title("💳 Fraud Analytics Dashboard")

# =====================================================
# Load Data
# =====================================================

summary = get_dashboard()

# Load enough rows for visualization
transactions = pd.DataFrame(
    get_transactions(limit=10000)
)

# =====================================================
# KPI Cards
# =====================================================

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

# =====================================================
# Pie Chart
# =====================================================

with chart1:

    st.subheader("Fraud Distribution")

    fraud_counts = pd.DataFrame({
        "Class": [
            "Legitimate",
            "Fraud"
        ],
        "Count": [
            summary["legitimate_cases"],
            summary["fraud_cases"]
        ]
    })

    fig = px.pie(
        fraud_counts,
        names="Class",
        values="Count",
        hole=0.45,
        title="Fraud vs Legitimate",
        color="Class",
        color_discrete_map={
            "Legitimate": "#2ECC71",
            "Fraud": "#E74C3C"
        }
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# Histogram
# =====================================================

with chart2:

    st.subheader("Transaction Amount Distribution")

    fig = px.histogram(
        transactions,
        x="amount",
        nbins=75,
        title="Transaction Amount Distribution",
        color_discrete_sequence=["#3498DB"]
    )

    fig.update_layout(
        xaxis_title="Transaction Amount ($)",
        yaxis_title="Number of Transactions"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )