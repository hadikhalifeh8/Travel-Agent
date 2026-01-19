import streamlit as st

def travel_inputs():
    st.markdown("### 🌍 Where are you headed?")
    source = st.text_input("🛫 Departure City (IATA Code):", "MEA")
    destination = st.text_input("🛬 Destination (IATA Code):", "FCO")

    st.markdown("### 📅 Plan Your Adventure")
    num_days = st.slider("🕒 Trip Duration (days):", 1, 14, 5)

    travel_theme = st.selectbox(
        "🎭 Select Your Travel Theme:",
        [
            "💑 Couple Getaway",
            "👨‍👩‍👧‍👦 Family Vacation",
            "🏔️ Adventure Trip",
            "🧳 Solo Exploration"
        ]
    )

    activity_preferences = st.text_area(
        "🌍 What activities do you enjoy?",
        "Relaxing on the beach, exploring historical sites"
    )

    departure_date = st.date_input("Departure Date")
    return_date = st.date_input("Return Date")

    return {
        "source": source,
        "destination": destination,
        "num_days": num_days,
        "travel_theme": travel_theme,
        "activities": activity_preferences,
        "departure_date": departure_date,
        "return_date": return_date
    }
