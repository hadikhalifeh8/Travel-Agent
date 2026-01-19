from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.serpapi import SerpApiTools

def build_planner(api_key):
    return Agent(
        name="Planner",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[SerpApiTools(api_key=api_key)],
        instructions=[
            "Gather details about the user's travel preferences and budget.",
            "Create a detailed itinerary with scheduled activities and estimated costs.",
            "Ensure the itinerary includes transportation options and travel time estimates.",
            "Optimize the schedule for convenience and enjoyment.",
            "Present the itinerary in a structured format."
        ]
    )