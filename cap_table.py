
import streamlit as st

def show_cap_table():
    st.subheader("📊 Cap Table Summary")

    founder_equity = 100
    investor_equity = 0

    if st.session_state.get("investor_log"):
        investor_equity = sum(o["equity"] for o in st.session_state.investor_log)
        founder_equity = max(0, 100 - investor_equity)

    bank_used = st.session_state.get("bank_used", False)

    st.markdown(f"""
    - 🧑 Founder: **{founder_equity}%**
    - 💸 Investors: **{investor_equity}%**
    - 🏦 Bank Loan: {"✅ Yes" if bank_used else "❌ No"}
    """)
