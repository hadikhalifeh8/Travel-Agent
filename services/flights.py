from serpapi import GoogleSearch

def fetch_flights(source, destination, departure, return_date, api_key):
    params = {
        "engine": "google_flights",
        "departure_id": source,
        "arrival_id": destination,
        "outbound_date": str(departure),
        "return_date": str(return_date),
        "currency": "USD",
        "hl": "en",
        "api_key": api_key
    }
    return GoogleSearch(params).get_dict()

def extract_cheapest_flights(data, limit=3):
    flights = data.get("best_flights", [])
    return sorted(flights, key=lambda x: x.get("price", 1e9))[:limit]

