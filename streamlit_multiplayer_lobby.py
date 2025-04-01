
import streamlit as st

def render_multiplayer_lobby():
    st.title("🎮 Multiplayer Role Lobby (Simulated)")
    st.write("Select your role in this simulation:")

    if st.button("Founder"):
        st.session_state.role = "Founder"
        st.session_state.page = "onboarding"
        st.rerun()

    if st.button("Investor"):
        st.session_state.role = "Investor"
        st.success("Investor dashboard coming soon...")

    if st.button("Supplier"):
        st.session_state.role = "Supplier"
        st.success("Supply negotiation module loading soon...")
