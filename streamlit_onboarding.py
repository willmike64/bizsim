
import streamlit as st
from generate_companies_withai import generate_startups, display_startups

def render_onboarding(navigate):
    st.title("🚀 Startup Acquisition Onboarding")
    st.markdown("Choose a startup to acquire based on financials, morale, and dependencies.")

    # Generate AI-powered startup data
    startups = generate_startups(n=15)

    if not startups or not isinstance(startups, list):
        st.error("❌ Failed to load startup data.")
        return

    display_startups(startups)

    selected = None
    for idx, company in enumerate(startups):
        if not isinstance(company, dict) or "name" not in company:
            continue
        if st.button(f"Acquire {company['name']}", key=f"select_{idx}"):
            selected = company
            break

    if selected:
        st.session_state.company_id = startups.index(selected) + 1
        st.session_state.selected_company = selected
        st.session_state.page = "funding_round"
        st.rerun()
