
import streamlit as st

def render_staffing_ui():
    st.subheader("👥 Staffing & Department Overview")

    departments = {
        "Sales": "Improve revenue through outreach",
        "Engineering": "Build and maintain products",
        "Marketing": "Increase brand awareness",
        "Customer Success": "Support and retain users",
        "Finance": "Manage capital and reporting"
    }

    st.markdown("### Department Status")

    for dept, desc in departments.items():
        with st.expander(dept):
            st.write(desc)
            hire = st.checkbox(f"📋 Hire in {dept}", key=f"hire_{dept}")
            if hire:
                st.success(f"✅ You have requested a hire in {dept}.")
