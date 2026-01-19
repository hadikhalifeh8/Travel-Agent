import streamlit as st

def sidebar_preferences():
    st.sidebar.title("🌎 Travel Assistant")
    st.sidebar.subheader("Personalize Your Trip")

    budget = st.sidebar.radio("💰 Budget Preference:", ["Economy", "Standard", "Luxury"])
    flight_class = st.sidebar.radio("✈️ Flight Class:", ["Economy", "Business", "First Class"])
    hotel_rating = st.sidebar.selectbox("🏨 Preferred Hotel Rating:", ["Any", "3⭐", "4⭐", "5⭐"])

    visa_required = st.sidebar.checkbox("🛃 Check Visa Requirements")
    travel_insurance = st.sidebar.checkbox("🛡️ Get Travel Insurance")

    return {
        "budget": budget,
        "flight_class": flight_class,
        "hotel_rating": hotel_rating,
        "visa_required": visa_required,
        "travel_insurance": travel_insurance
    }
