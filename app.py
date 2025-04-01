
import streamlit as st
from reset import reset_simulation
import streamlit_lobby as lobby
import streamlit_onboarding as onboarding
import streamlit_funding_round as funding_round
import streamlit_ceo_dashboard as ceo_dashboard
import streamlit_ceo_decisions as ceo_decisions
import streamlit_founder_dashboard as investor_view
import streamlit_company_list as company_list
import streamlit_generate_companies as company_generator
import stock_ticker_banner as news_banner
import staffing
import cap_table
import term_sheet
from logger import log_event

if "page" not in st.session_state:
    st.session_state.page = "intro"
    log_event("🔁 App started - entering intro page")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "mode" not in st.session_state:
    st.session_state.mode = None
if "role" not in st.session_state:
    st.session_state.role = None
if "company_id" not in st.session_state:
    st.session_state.company_id = None
if "funding_complete" not in st.session_state:
    st.session_state.funding_complete = False

with st.sidebar:
    st.title("🧭 Sim Controls")
    st.write("Page:", st.session_state.page)
    st.write("Role:", st.session_state.role)
    st.write("Company ID:", st.session_state.company_id)
    if st.button("🔄 Reset Simulation"):
        log_event("🔁 Simulation manually reset")
        reset_simulation()

def navigate(page):
    log_event(f"➡️ Navigating to: {page}")
    st.session_state.page = page
    st.rerun()

if st.session_state.page == "intro":
    st.title("💼 Startup Simulation")
    player_name = st.text_input("Enter your name to start:", key="player_name")
    if st.button("Login / Start"):
        st.session_state.logged_in = True
        log_event(f"✅ Player logged in as: {player_name}")
        navigate("lobby")

elif st.session_state.page == "lobby":
    log_event("🏁 In Lobby")
    if st.session_state.mode == "single" and not st.session_state.role:
        lobby.render_role_picker(navigate)
    elif st.session_state.mode == "single" and st.session_state.role:
        navigate("onboarding")
    else:
        lobby.render_lobby(navigate)

elif st.session_state.page == "onboarding":
    log_event("🚀 Entered onboarding flow")
    onboarding.render_onboarding(navigate)

elif st.session_state.page == "funding_round":
    log_event("💸 Entered funding round")
    funding_round.render_funding_ui(navigate)

elif st.session_state.page == "single_player":
    if not st.session_state.funding_complete:
        navigate("funding_round")
    elif st.session_state.role == "CEO":
        log_event("👔 CEO view initialized")
        ceo_dashboard.render_ceo_ui()
        ceo_decisions.render_decision_ui()
        staffing.render_staffing_ui()
        cap_table.show_cap_table()
        term_sheet.show_term_sheet()
        news_banner.render_news()
    elif st.session_state.role == "Investor":
        log_event("📈 Investor view initialized")
        investor_view.render_investor_ui()
        news_banner.render_news()
    else:
        st.warning("Unknown role. Returning to lobby.")
        navigate("lobby")
