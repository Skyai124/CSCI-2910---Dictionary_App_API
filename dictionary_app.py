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

#displays the word and its definitions, phonetics, synonyms, and antonyms in a formatted way
def display_word(data: list):
    entry = data[0]
    word = entry.get("word", "")
    phonetics = entry.get("phonetics", [])
    meanings = entry.get("meanings", [])

    print("\n" + ("====================================================================="))
    print(f"  {word.upper()}")
    for ph in phonetics:
        if ph.get("text"):
            print(f"  {ph['text']}")
            break
    print("=====================================================================")

    for meaning in meanings:
        part = meaning.get("partOfSpeech", "")
        definitions = meaning.get("definitions", [])
        synonyms = meaning.get("synonyms", [])
        antonyms = meaning.get("antonyms", [])

        print(f"\n[{part.upper()}]")
        for i, defn in enumerate(definitions[:3], 1):
            print(f"  {i}. {defn.get('definition', '')}")
            if defn.get("example"):
                print(f'     e.g. "{defn["example"]}"')
        if synonyms:
            print(f"  Synonyms: {', '.join(synonyms[:5])}")
        if antonyms:
            print(f"  Antonyms: {', '.join(antonyms[:5])}")
    print()

# saves the history of the words that have been looked up to a json file called lookup_history.json
