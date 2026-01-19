import streamlit as st
from services.formatter import format_datetime

def show_flights(flights):
    st.subheader("✈️ Cheapest Flight Options")

    if not flights:
        st.warning("No flight data available.")
        return

    cols = st.columns(len(flights))
    for idx, flight in enumerate(flights):
        with cols[idx]:
            price = flight.get("price", "N/A")
            duration = flight.get("total_duration", "N/A")

            flights_info = flight.get("flights", [{}])
            departure = flights_info[0].get("departure_airport", {})
            arrival = flights_info[-1].get("arrival_airport", {})

            st.markdown(f"""
            **💰 Price:** {price}  
            **🕒 Duration:** {duration} min  
            **🛫 Departure:** {format_datetime(departure.get("time", ""))}  
            **🛬 Arrival:** {format_datetime(arrival.get("time", ""))}
            """)
