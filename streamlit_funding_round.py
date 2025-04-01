
import streamlit as st

def render_funding_ui(navigate):
    company = st.session_state.get("selected_company")
    if not company:
        st.warning("No company selected. Returning to onboarding.")
        st.session_state.page = "onboarding"
        st.rerun()

    if "negotiation_stage" not in st.session_state:
        st.session_state.negotiation_stage = "owner"
    if "owner_round" not in st.session_state:
        st.session_state.owner_round = 1
    if "owner_offer" not in st.session_state:
        st.session_state.owner_offer = {
            "valuation": int(company["valuation"] * 1.2),
            "equity": 100
        }
    if "user_offer" not in st.session_state:
        st.session_state.user_offer = {
            "valuation": company["valuation"],
            "equity": 100
        }
    if "owner_agreed" not in st.session_state:
        st.session_state.owner_agreed = False
    if "investor_round" not in st.session_state:
        st.session_state.investor_round = 1
    if "investor_offer" not in st.session_state:
        st.session_state.investor_offer = {
            "amount": int(company["funding_need"] * 0.8),
            "equity": 20
        }
    if "funds_raised" not in st.session_state:
        st.session_state.funds_raised = 0
    if "acquisition_signed" not in st.session_state:
        st.session_state.acquisition_signed = False

    st.subheader(f"🏢 Company: {company['name']}")
    st.caption(f"Negotiation Stage: {st.session_state.negotiation_stage.upper()}")

    if st.session_state.negotiation_stage == "owner":
        st.header("🤝 Negotiation with Original Owner")
        st.write(f"🧾 Asking Price: ${st.session_state.owner_offer['valuation']:,}")
        st.write(f"🎯 Equity Offered: {st.session_state.owner_offer['equity']}%")

        user_val = st.number_input("Your Valuation Offer ($)", min_value=100000, step=100000, value=st.session_state.user_offer["valuation"])
        if st.button("Submit Offer to Original Owner"):
            st.session_state.user_offer["valuation"] = user_val
            st.session_state.owner_round += 1

            midpoint = int((user_val + st.session_state.owner_offer["valuation"]) / 2)
            st.session_state.owner_offer["valuation"] = midpoint

            if abs(user_val - st.session_state.owner_offer["valuation"]) < 250000 or st.session_state.owner_round > 10:
                st.success("✅ Deal agreed in principle with the Original Owner.")
                st.session_state.owner_agreed = True
                st.session_state.negotiation_stage = "investors"
                st.rerun()

    elif st.session_state.negotiation_stage == "investors":
        st.header("💸 Negotiation with AI Investors (Fundraising)")
        st.write(f"🏁 Goal: Raise ${company['funding_need']:,} to acquire {company['name']}")
        st.write(f"💰 AI Investor Offer: ${st.session_state.investor_offer['amount']:,} for {st.session_state.investor_offer['equity']}% equity")

        if st.button("Accept Investor Offer"):
            st.session_state.funds_raised += st.session_state.investor_offer["amount"]
            st.session_state.investor_round += 1

            new_amount = int(st.session_state.investor_offer["amount"] * 0.95)
            new_equity = min(st.session_state.investor_offer["equity"] + 2, 100)
            st.session_state.investor_offer = {
                "amount": new_amount,
                "equity": new_equity
            }

            if st.session_state.funds_raised >= company["funding_need"]:
                st.success("🎉 You have raised enough to acquire the company!")
                st.session_state.acquisition_signed = True
                st.session_state.funding_complete = True
                st.session_state.page = "single_player"
                st.rerun()
            elif st.session_state.investor_round > 10:
                st.error("❌ Failed to raise enough funds. Returning to onboarding.")
                st.session_state.page = "onboarding"
                st.rerun()

    else:
        st.warning("Unknown negotiation state. Resetting.")
        st.session_state.page = "onboarding"
        st.rerun()
