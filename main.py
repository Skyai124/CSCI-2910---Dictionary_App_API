from dictionary_app import fetch_word, display_word, load_history, save_history

def main():
    print("=====================================================================")
    print("     ENGLISH DICTIONARY  —  dictionaryapi.dev")
    print("=====================================================================")
    print("Commands:  <word>  |  history  |  clear  |  save  |  quit")
    
    # The 'history' command shows the list of words you've looked up.
    # The 'clear' command clears the history.
    history = load_history()
