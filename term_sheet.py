
import streamlit as st

def show_term_sheet():
    st.subheader("📄 Term Sheet Preview")

    company = st.session_state.get("selected_company")
    investor_log = st.session_state.get("investor_log", [])
    bank_used = st.session_state.get("bank_used", False)
    bank_offer = st.session_state.get("bank_offer", {})

    st.markdown("### 🚀 Acquisition Target")
    st.write(f"Company: {company['name']}")
    st.write(f"Valuation: ${company['valuation']:,}")

    st.markdown("### 💸 Investor Agreements")
    for i, inv in enumerate(investor_log, 1):
        st.write(f"Round {i}: ${inv['amount']:,} for {inv['equity']}% equity")

    if bank_used:
        st.markdown("### 🏛️ Bank Loan")
        st.write(f"${bank_offer['amount']:,} at {bank_offer['interest']}% interest")

    if not st.session_state.get("term_sheet_signed"):
        if st.button("✍️ Sign Term Sheet"):
            st.session_state.term_sheet_signed = True
            st.success("✅ Term Sheet Signed. You now officially control the company!")
