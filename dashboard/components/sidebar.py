import streamlit as st


def render_sidebar():

    """st.sidebar.image(
        "assets/logo.png",
        use_container_width=True
    )"""

    st.sidebar.title("Fraud Analytics")

    st.sidebar.caption(
        "AI Powered Fraud Detection Platform"
    )

    st.sidebar.divider()

    page = st.sidebar.radio(

        "Navigation",

        [

            "Dashboard",

            "Analytics",

            "Transactions",

            "AI Predictor",

            "Model Performance",

            "Settings"

        ]

    )

    st.sidebar.divider()

    st.sidebar.success(
        "Backend Connected"
    )

    st.sidebar.caption(
        "Version 2.0"
    )

    return page