
import streamlit as st
from streamlit_generate_companies_withai import generate_startups, display_startups

def render_onboarding(navigate):
    st.subheader("🚀 Choose a Company to Acquire")

    startups = generate_startups(n=15)

    display_startups(startups)

    for idx, company in enumerate(startups):
        if st.button(f"Select {company['name']}", key=f"select_{idx}"):
            st.session_state.company_id = idx + 1
            st.session_state.selected_company = company
            st.session_state.page = "funding_round"
            st.rerun()
