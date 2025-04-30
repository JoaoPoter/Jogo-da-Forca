HANGMAN_PICS = [
    """
     +-----+
           |
           |
           |
           |
          ===""",
    """
     +-----+
     O     |
           |
           |
           |
          ===""",
    """
     +-----+
     O     |
     |     |
           |
           |
          ===""",
    """
     +-----+
     O     |
    /|     |
           |
           |
          ===""",
    """
     +-----+
     O     |
    /|\    |
           |
           |
          ===""",
    """
     +-----+
     O     |
    /|\    |
    /      |
           |
          ===""",
    """
     +-----+
     O     |
    /|\    |
    / \    |
           |
          ==="""
]

# Function to display the hangman based on the number of wrong guesses
def display_hangman(errors):
    print(HANGMAN_PICS[errors])
