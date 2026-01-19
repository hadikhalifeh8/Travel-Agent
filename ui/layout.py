import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="🌍 AI Travel Planner",
        layout="wide"
    )

    st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #ff5733;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">✈️ AI-Powered Travel Planner</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Plan your dream trip with AI! Flights, Hotels & Itineraries.</p>',
        unsafe_allow_html=True
    )
