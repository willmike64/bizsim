def render_lobby(navigate):
 import streamlit as st
 st.write('🎮 Welcome to the Simulation Lobby')
 if st.button('Single-Player Mode'):
  st.session_state.mode = 'single'
  navigate('lobby')
 if st.button('Multiplayer Mode'):
  st.session_state.mode = 'multi'
  navigate('multiplayer')

def render_role_picker(navigate):
 import streamlit as st
 st.subheader('Choose Your Role')
 if st.button('CEO'):
  st.session_state.role = 'CEO'
  navigate('onboarding')
 if st.button('Investor'):
  st.session_state.role = 'Investor'
  navigate('onboarding')