
import streamlit as st

def render_onboarding(navigate):
    st.subheader("🚀 Choose a Company to Acquire")

    companies = [
        {"id": 1, "name": "SmartHome AI", "industry": "IoT/Consumer Tech", "valuation": 3000000, "funding_need": 1000000},
        {"id": 2, "name": "BioHealthX", "industry": "Healthcare Biotech", "valuation": 5000000, "funding_need": 2000000},
        {"id": 3, "name": "GreenEnergy Grid", "industry": "Renewable Energy", "valuation": 4500000, "funding_need": 1500000}
    ]

    for company in companies:
        with st.expander(f"{company['name']} — {company['industry']}"):
            st.write(f"💰 Valuation: ${company['valuation']:,}")
            st.write(f"📊 Capital Needed: ${company['funding_need']:,}")
            if st.button(f"Select {company['name']}", key=company["id"]):
                st.session_state.company_id = company["id"]
                st.session_state.selected_company = company
                st.session_state.page = "funding_round"
                st.rerun()
