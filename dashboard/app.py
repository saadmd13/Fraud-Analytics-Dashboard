import streamlit as st

from components.sidebar import render_sidebar

from views.dashboard import dashboard_page
from views.analytics import analytics_page
from views.transactions import transactions_page
from views.predictor import predictor_page
from views.model_performance import performance_page
from views.settings import settings_page

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Fraud Analytics Platform",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# Sidebar
# =====================================================

page = render_sidebar()

# =====================================================
# Navigation
# =====================================================

if page == "Dashboard":

    dashboard_page()

elif page == "Analytics":

    analytics_page()

elif page == "Transactions":

    transactions_page()

elif page == "AI Predictor":

    predictor_page()

elif page == "Model Performance":

    performance_page()

elif page == "Settings":

    settings_page()