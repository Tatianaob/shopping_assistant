from serpapi import GoogleSearch

def search_products(query):
    search = GoogleSearch({
        "q": query,
        "tbm": "shop",
        "api_key": "My API key"  # Replace with SerpAPI key
    })
    results = search.get_dict()
    return results.get("shopping_results", [])