import streamlit as st

def init_session_state():
    defaults = {
        "page": "intro",
        "mode": "single",
        "role": None,
        "company_id": None,
        "funding_complete": False,
        "results_df": None,
        "log_data": []
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
