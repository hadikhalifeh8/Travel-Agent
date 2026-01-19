from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.serpapi import SerpApiTools

def build_hotel_restaurant_finder(api_key):
    return Agent(
        name="Hotel & Restaurant Finder",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[SerpApiTools(api_key=api_key)],
        instructions=[
            "Identify key locations in the user's travel itinerary.",
            "Search for highly rated hotels near those locations.",
            "Search for top-rated restaurants based on cuisine preferences and proximity.",
            "Prioritize results based on user preferences, ratings, and availability.",
            "Provide direct booking links or reservation options where possible."
        ]
    )