
import streamlit as st

def show_cap_table():
    st.subheader("📊 Cap Table Summary")
    founder_equity = 100

    if st.session_state.get("investor_log"):
        investor_equity = sum(o["equity"] for o in st.session_state.investor_log)
        founder_equity -= investor_equity
    else:
        investor_equity = 0

    st.markdown(f"""
    - 🧑 Founder: **{founder_equity}%**
    - 💸 Investors: **{investor_equity}%**
    - 🏦 Bank Loan: {'✅ Yes' if st.session_state.get('bank_used') else '❌ No'}
    """)
