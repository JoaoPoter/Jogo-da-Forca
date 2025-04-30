import os
import time
from hangman import display_hangman
os.system("cls")

while True:
    challenger = "shark"
    competitor = "pog"
    errors = 0
    time.sleep(0)
    os.system("cls")

    keyword = "pong"
    hint1 = "game"
    hint2 = "atari"
    hint3 = "ball"
    hints = [hint1, hint2, hint3]
    hint_index = 0
    hint_used = False
    attempted_letters = []
    time.sleep(0)
    os.system("cls")

    asterisks = '*' * len(keyword)

    while True:
        os.system("cls")
        print(f"Word by {challenger}: {asterisks}")
        print(f"Attempted letters: {', '.join(attempted_letters)}")
        display_hangman(errors)
        attempt = input(f"{competitor} can guess a letter and the word{'' if hint_used else f' or see hint {hint_index+1}'}: ")
        
        if attempt in attempted_letters:
            print(f"You've already tried the letter '{attempt}'. Try a different one.")
            time.sleep(2)
            continue

        if attempt == 'hint' and not hint_used:
            if hint_index < len(hints):
                print(f"Hint {hint_index + 1}: {hints[hint_index]}")
                hint_index += 1
                hint_used = True
                time.sleep(2)
            elif hint_index == len(hints):
                 hint_used = True
                 print("No more hints available.")
            continue
        elif len(attempt) == 1 and attempt.isalpha():
            attempted_letters.append(attempt)
            if not hint_index == len(hints):
                hint_used = False
            if attempt in keyword:
                print(f"Nice {competitor}! The letter '{attempt}' is in the word.")
                for c in keyword:
                    if c == attempt:
                        asterisks = asterisks[:keyword.index(c)] + c + asterisks[keyword.index(c) + 1:]
                print(f"Word: {asterisks}")
                time.sleep(2)
                os.system("cls")
                if asterisks == keyword:
                    print(f"Congratulations {competitor}! You guessed the word '{keyword}'!")
                    time.sleep(2)
                    print("and you where this close to death!")
                    display_hangman(errors)
                    time.sleep(2)
                    break
            else:  
                print(f"Sorry, the letter '{attempt}' is not in the word.")
                errors += 1
                print(f"Errors: {errors}")
                time.sleep(2)
                os.system("cls")
                if errors == 6:
                    display_hangman(errors)
                    print(f"Game Over! The word was '{keyword}'.")
                    time.sleep(2)
                    print(f"Congratulations {challenger}! You won!")
                    time.sleep(2.5)
                    break
        else:
            if attempt == keyword:
                print(f"Congratulations {competitor}! You guessed the word '{keyword}'!")
                time.sleep(2)
                print("and you where this close to death!")
                display_hangman(errors)
                time.sleep(2)
                break
            
            elif hint_index == len(hints):
                 hint_used = True
                 print("No more hints available.")
                 time.sleep(2)
            elif attempt == "hint" and hint_used and hint_index < len(hints):
                print("Hint already used.")
                time.sleep(2)
            else:
                os.system("cls")
                print("Invalid input. Please enter a single letter or 'hint'.")
                time.sleep(2.5)
            continue