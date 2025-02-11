from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def search_products(query):
    search = GoogleSearch({
        "q": query,
        "tbm": "shop",
        "api_key": os.getenv("SERPAPI_KEY")  # Get the API key from the environment variable
    })
    results = search.get_dict()
    return results.get("shopping_results", [])
