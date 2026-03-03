import requests
import json
API_BASE = "https://api.dictionaryapi.dev/api/v2/entries/en"
# this api calls from a database that contains all English words 
# It is a free API that does not require an API key in any way.

#fetches the word from the API and returns the data and error message if there is one
def fetch_word(word: str):
    url = f"{API_BASE}/{word.strip().lower()}"
    response = requests.get(url)
    if response.status_code == 404:
        return None, "Word not found. Please check your spelling."
    if response.status_code != 200:
        return None, f"API error: HTTP {response.status_code}"
    return response.json(), None
