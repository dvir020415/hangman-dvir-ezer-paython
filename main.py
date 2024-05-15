import random


# Function to check if the guessed letter is valid
def check_valid_input(letter_guessed, old_letters_guessed):
    # Check if the guessed letter is a single alphabetic character and hasn't been guessed before
    if len(letter_guessed) != 1 or not letter_guessed.isalpha() or letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


# Function to update the list of guessed letters if the input is valid
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


# Function to display the current state of the secret word
def show_hidden_word(secret_word, old_letters_guessed):
    displayed_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


# Function to check if the player has won
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


# Function to print the hangman status based on the number of incorrect attempts
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {
        0: """
        x-------x
        |
        |
        |
        |
        |
        """,
        1: """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
        2: """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
        3: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
        4: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,
        5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
    }
    print(HANGMAN_PHOTOS[num_of_tries])


# Function to choose a word from the file based on the provided index
def choose_word(index):
    # Read the words from the text file
    with open(r'C:\Users\ezer8\Desktop\words.text.txt', 'r') as file:
        words = file.read().split()

    # Get the number of unique words
    num_unique_words = len(set(words))

    # Choose the word based on the index
    chosen_word_index = (index - 1) % len(words)
    chosen_word = words[chosen_word_index]

    return num_unique_words, chosen_word


# Define constants
MAX_TRIES = 6


# Define the main function
def main():
    # ASCII art for the game
    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""

    print(HANGMAN_ASCII_ART)
    # Welcome message and instructions
    print("Welcome to Hangman!")
    print("Try to guess the secret word by guessing one letter at a time.")
    print("You have 6 attempts to guess the word correctly.")

    # Get the index of the word from the player
    index = int(input("Enter the index of the word you want to use: "))

    # Choose the secret word from the file
    num_of_words, secret_word = choose_word(index)

    # Initialize variables
    old_letters_guessed = []
    num_of_tries = 0

    # Start the game loop
    while num_of_tries < MAX_TRIES:
        # Print hangman status
        print_hangman(num_of_tries)

        # Print the current hidden word
        print(show_hidden_word(secret_word, old_letters_guessed))

        # Ask the player for a letter
        letter_guessed = input("Guess a letter: ").lower()

        # Check if the guessed letter is valid
        if check_valid_input(letter_guessed, old_letters_guessed):
            # Try updating the guessed letters
            if try_update_letter_guessed(letter_guessed, old_letters_guessed):
                # Check if the player has won
                if check_win(secret_word, old_letters_guessed):
                    print("Congratulations! You guessed the word:", secret_word)
                    break
                # Check if the guessed letter is in the secret word
                if letter_guessed in secret_word:
                    continue
                else:
                    # Letter guessed incorrectly
                    print("Letter guessed incorrectly.")
                    num_of_tries += 1
            else:
                # Letter is not valid
                print("Letter is not valid.")
        else:
            # Invalid input
            print("Invalid input. Please guess a single letter that you haven't guessed before.")

    # If the loop ends without breaking, the player loses
    else:
        print_hangman(MAX_TRIES)
        print("Sorry, you ran out of attempts. The word was:", secret_word)


# Call the main function
if __name__ == "__main__":
    main()