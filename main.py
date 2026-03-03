from dictionary_app import fetch_word, display_word, load_history, save_history

def main():
    print("=====================================================================")
    print("     ENGLISH DICTIONARY  —  dictionaryapi.dev")
    print("=====================================================================")
    print("Commands:  <word>  |  history  |  clear  |  save  |  quit")
    
    # The 'history' command shows the list of words you've looked up.
    # The 'clear' command clears the history.
    history = load_history()

while True:
        try:
            user_input = input("\nEnter a word: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        cmd = user_input.lower()

        if cmd == "quit":
            print("Goodbye!")
            break
        elif cmd == "history":
            if not history:
                print("No lookups yet.")
            else:
                for i, w in enumerate(history, 1):
                    print(f"  {i}. {w}")
        elif cmd == "clear":
            history = []
            print("History cleared.")
        elif cmd == "save":
            save_history(history)
        else:
            print(f"Looking up '{user_input}'...")
            data, error = fetch_word(user_input)
            if error:
                print(f"  ✗ {error}")
            else:
                display_word(data)
                word = data[0].get("word", user_input)
                if word not in history:
                    history.append(word)

if __name__ == "__main__":
    main()
