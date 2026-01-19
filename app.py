import streamlit as st
import json

# CONFIG
from config.settings import SERPAPI_KEY

# UI
from ui.layout import setup_page
from ui.inputs import travel_inputs
from ui.sidebar import sidebar_preferences
from ui.results import show_flights

# SERVICES
from services.flights import fetch_flights, extract_cheapest_flights

# AGENTS
from agents.researcher import build_researcher
from agents.planner import build_planner
from agents.hotel_finder import build_hotel_restaurant_finder


# --------------------------------------------------
# PAGE SETUP
# --------------------------------------------------
setup_page()

# --------------------------------------------------
# USER INPUTS
# --------------------------------------------------
inputs = travel_inputs()
preferences = sidebar_preferences()

# --------------------------------------------------
# AI AGENTS
# --------------------------------------------------
researcher = build_researcher(SERPAPI_KEY)
planner = build_planner(SERPAPI_KEY)
hotel_agent = build_hotel_restaurant_finder(SERPAPI_KEY)


# --------------------------------------------------
# 🚀 GENERATE TRAVEL PLAN (MAIN LOGIC)
# --------------------------------------------------
if st.button("🚀 Generate Travel Plan"):

    # -----------------------------
    # FLIGHTS
    # -----------------------------
    with st.spinner("✈️ Fetching best flight options..."):
        flight_data = fetch_flights(
            inputs["source"],
            inputs["destination"],
            inputs["departure_date"],
            inputs["return_date"],
            SERPAPI_KEY
        )
        cheapest_flights = extract_cheapest_flights(flight_data)

    show_flights(cheapest_flights)

    # -----------------------------
    # RESEARCH AGENT
    # -----------------------------
    with st.spinner("🔍 Researching attractions & activities..."):
        research_prompt = f"""
        Research the best attractions and activities in {inputs['destination']}
        for a {inputs['num_days']}-day {inputs['travel_theme'].lower()} trip.

        Traveler interests: {inputs['activities']}
        Budget: {preferences['budget']}
        Flight class: {preferences['flight_class']}
        Hotel rating: {preferences['hotel_rating']}
        Visa required: {preferences['visa_required']}
        Travel insurance: {preferences['travel_insurance']}
        """

        research_results = researcher.run(research_prompt, stream=False)

    # -----------------------------
    # HOTEL & RESTAURANT AGENT
    # -----------------------------
    with st.spinner("🏨 Searching hotels & restaurants..."):
        hotel_prompt = f"""
        Find the best hotels and restaurants near popular attractions in
        {inputs['destination']}.

        Budget: {preferences['budget']}
        Hotel rating: {preferences['hotel_rating']}
        Preferred activities: {inputs['activities']}
        """

        hotel_results = hotel_agent.run(hotel_prompt, stream=False)

    # -----------------------------
    # PLANNER AGENT
    # -----------------------------
    with st.spinner("🗺️ Creating itinerary..."):
        planning_prompt = f"""
        Create a {inputs['num_days']}-day itinerary for a
        {inputs['travel_theme'].lower()} trip to {inputs['destination']}.

        Interests: {inputs['activities']}
        Budget: {preferences['budget']}
        Flight class: {preferences['flight_class']}
        Hotel rating: {preferences['hotel_rating']}
        Visa: {preferences['visa_required']}
        Insurance: {preferences['travel_insurance']}

        Research:
        {research_results.content}

        Flights:
        {json.dumps(cheapest_flights)}

        Hotels & Restaurants:
        {hotel_results.content}
        """

        itinerary = planner.run(planning_prompt, stream=False)

    # -----------------------------
    # DISPLAY RESULTS
    # -----------------------------
    st.subheader("🏨 Hotels & Restaurants")
    st.write(hotel_results.content)

    st.subheader("🗺️ Your Personalized Itinerary")
    st.write(itinerary.content)

    st.success("✅ Travel plan generated successfully!")
