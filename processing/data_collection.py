# data_collection.py
# Author: Adam Messick
# Date: 5/24/2023

import json
from serpapi import GoogleSearch

def perform_search(query, location, api_key):
    """Perform a custom Google search using the SerpAPI."""
    try:
        params = {
            "q": query,
            "location": location,
            "api_key": api_key,
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return results
    except Exception as e:
        print(f"An error occurred while performing the search: {e}")

if __name__ == "__main__":
    # An example of using the function
    api_key = "Your_SerpAPI_Key_Here"
    query = "OpenAI"
    location = "Austin, Texas"

    search_results = perform_search(query, location, api_key)
    print(json.dumps(search_results, indent=2))
