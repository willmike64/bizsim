import openai
import streamlit as st
import random
import ast
from typing import List, Dict

openai.api_key = st.secrets["OPENAI_API_KEY"]

industries = [
    "AgTech", "EdTech", "HealthTech", "Clean Energy", "SaaS",
    "Consumer Goods", "eCommerce", "Biotech", "AI Tools", "Food Delivery",
    "Logistics", "RetailTech", "Greentech", "Mobility", "Digital Wellness", "Coffee Shop", "Local Restaurant",
    "Fitness", "Real Estate", "TravelTech", "Fintech", "Manufacturing",
    "Construction", "Gaming", "Entertainment", "Telecom", "Cybersecurity",
    "Insurance", "LegalTech", "HRTech", "PropTech", "Blockchain",
    "Social Media", "Wearables", "Augmented Reality", "Virtual Reality",
    "Elder Care", "Pet Tech", "Travel", "Home Services", "Subscription Boxes",
    "Food & Beverage", "Fashion", "Beauty", "Sports", "Wellness",
    "Nonprofit", "Crowdfunding", "Digital Marketing", "Advertising",
    "Content Creation", "Influencer Marketing", "Event Planning", "Public Relations",
    "Market Research", "Data Analytics", "Artificial Intelligence",
    "Machine Learning", "Natural Language Processing", "Computer Vision",
    "Robotics", "Internet of Things", "Smart Home", "Smart City",
    "Telemedicine", "Health & Wellness", "Fitness & Nutrition",
    "Mental Health", "Personal Finance", "Investment", "Cryptocurrency",
    "Real Estate Investment", "Crowdfunding", "Peer-to-Peer Lending",
    "Wealth Management", "Insurance Tech", "RegTech", "Compliance",
    "Supply Chain", "Logistics & Transportation", "Fleet Management",
    "Last Mile Delivery", "E-commerce Logistics", "Warehouse Management",
    "Inventory Management", "Shipping & Freight", "Cold Chain Logistics",
    "Reverse Logistics", "Freight Forwarding", "Customs Brokerage",
    "Supply Chain Finance", "Procurement", "Sourcing", "Vendor Management",
    "Contract Management", "Spend Analysis", "Supplier Relationship Management",
    "Demand Planning", "Forecasting", "Production Planning",
    "Quality Control", "Manufacturing Execution", "Lean Manufacturing",
    "Six Sigma", "Total Quality Management", "Continuous Improvement",
    "Just-in-Time Manufacturing", "Agile Manufacturing", "Flexible Manufacturing",
    "Mass Customization", "Additive Manufacturing", "3D Printing",
    "Robotics Process Automation", "Industrial Internet of Things",
    "Smart Manufacturing", "Digital Twin", "Cyber-Physical Systems",
    "Advanced Manufacturing", "Sustainable Manufacturing",
    "Circular Economy", "Green Manufacturing", "Eco-Design"
]

def generate_startups(n: int = 15) -> List[Dict]:
    prompt = f"""Create {n} fictional startup companies. For each, include:
- name
- industry (from: {', '.join(industries[:15])})
- short description
- estimated valuation (in USD)
- morale score (0–100)
- customers
- a list of 3 dependencies (supply chain)

Return as a Python list of dictionaries.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0.7,
            max_tokens=1500
        )
        startup_list = ast.literal_eval(response.choices[0].message["content"])
        return startup_list
    except Exception as e:
        return fallback_startups() + [{"error": str(e)}]

def fallback_startups() -> List[Dict]:
    return [{
        "name": "Fallback Co.v1",
        "industry": "EdTech",
        "description": "This is a fallback startup shown when OpenAI fails.",
        "valuation": "$1,000,000",
        "revenue": "$250,000",
        "ebitda": "$50,000",
        "assets": "$300,000",
        "debt": "$20,000",
        "morale": 75,
        "customers": 1200,
        "dependencies": ["Servers", "Content Creators", "Marketing"]
    }]

def display_startups(startups: List[Dict]):
    st.subheader("🚀 Startup Opportunities")

    for s in startups:
        # Safely skip malformed entries
        if not isinstance(s, dict) or "name" not in s or "industry" not in s:
            st.warning("⚠️ Skipping invalid startup entry.")
            continue

        with st.expander(f"{s['name']} — {s['industry']}"):
            st.write(s.get('description', 'No description provided.'))
            st.metric("💰 Valuation", s.get('valuation', 'N/A'))
            st.metric("📈 Revenue", s.get('revenue', 'N/A'))
            st.metric("💹 EBITDA", s.get('ebitda', 'N/A'))
            st.metric("🏦 Assets", s.get('assets', 'N/A'))
            st.metric("💸 Debt", s.get('debt', 'N/A'))
            st.metric("📊 Morale", s.get('morale', 'N/A'))
            st.metric("👥 Customers", s.get('customers', 'N/A'))
            st.write("📦 Dependencies:", ', '.join(s.get('dependencies', [])))