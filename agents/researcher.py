from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.serpapi import SerpApiTools

def build_researcher(api_key):
    return Agent(
        name="Researcher",
        model=Gemini(id="gemini-2.5-flash"),
        tools=[SerpApiTools(api_key=api_key)],
        instructions=[
            "Identify the travel destination specified by the user.",
            "Gather detailed information on the destination, including climate, culture, and safety tips.",
            "Find popular attractions, landmarks, and must-visit places.",
            "Search for activities that match the user’s interests and travel style.",
            "Prioritize information from reliable sources and official travel guides.",
            "Provide well-structured summaries with key insights and recommendations."
        ]
    )
