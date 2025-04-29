import os
import time
from hangman import display_hangman

# --- constantes ---
MAX_ERRORS = 6
REFRESH_DELAY = 2

# --- funções utilitárias ---
def clear():
    os.system("cls")

def sleep():
    time.sleep(REFRESH_DELAY)

# --- renderização ---
def render(hidden, attempts, errors, challenger, competitor):
    clear()
    print(f"Word by {challenger}: {hidden}")
    print(f"Attempted letters: {', '.join(attempts)}")
    display_hangman(errors)

# --- entrada do jogador ---
def get_input(competitor, hint_index, hint_available):
    prompt = f"{competitor}, digite uma letra, uma palavra ou "
    prompt += f"'hint' (dica {hint_index+1})" if hint_available else ""
    return input(prompt + ": ").strip().lower()

# --- tratamento de dicas ---
def process_hint(hints, hint_index, hint_used):
    if hint_index < len(hints) and not hint_used:
        print(f"Dica {hint_index+1}: {hints[hint_index]}")
        return hint_index+1, True
    elif hint_used:
        print("Você precisa chutar antes de pedir outra dica.")
    else:
        print("Não há mais dicas disponíveis.")
    return hint_index, hint_used

# --- tratamento de letra única ---
def process_letter(attempt, keyword, hidden, attempts, errors, competitor):
    attempts.append(attempt)
    # revela todas as ocorrências corretamente
    new_hidden = list(hidden)
    for idx, c in enumerate(keyword):
        if c == attempt:
            new_hidden[idx] = attempt
    new_hidden = "".join(new_hidden)

    if new_hidden != hidden:
        print(f"Boa, '{attempt}' está na palavra!")
    else:
        print(f"'{attempt}' não está na palavra.")
        errors += 1

    print(f"Erros: {errors}")
    return new_hidden, errors

# --- tratamento de palavra inteira ---
def process_word(attempt, keyword, errors, competitor):
    if attempt == keyword:
        print(f"Parabéns {competitor}! Você adivinhou a palavra '{keyword}'!")
        return True, errors
    else:
        print(f"'{attempt}' não é a palavra correta.")
        errors += 1
        print(f"Erros: {errors}")
        return False, errors

# --- loop principal ---
def main():
    challenger = "shark"
    competitor = "pog"

    keyword = "pong"
    hints = ["game", "atari", "ball"]

    while True:
        errors = 0
        hint_index = 0
        hint_used = False
        attempted_letters = []
        hidden = "*" * len(keyword)

        while True:
            render(hidden, attempted_letters, errors, challenger, competitor)
            attempt = get_input(competitor, hint_index, hint_index < len(hints))

            # validação básica
            if not attempt.isalpha():
                print("Entrada inválida. Use apenas letras.")
                sleep()
                continue

            # comando de dica
            if attempt == "hint":
                hint_index, hint_used = process_hint(hints, hint_index, hint_used)
                sleep()
                continue

            # palpite de letra
            if len(attempt) == 1:
                if attempt in attempted_letters:
                    print(f"'{attempt}' já foi tentada.")
                    sleep()
                    continue
                hidden, errors = process_letter(attempt, keyword, hidden, attempted_letters, errors, competitor)
                hint_used = False  # libera próxima dica
                sleep()
            # palpite de palavra
            else:
                won, errors = process_word(attempt, keyword, errors, competitor)
                sleep()
                if won:
                    display_hangman(errors)
                    sleep()
                    break

            # checa vitória ou derrota
            if hidden == keyword:
                print(f"Parabéns {competitor}! Palavra '{keyword}' completa!")
                display_hangman(errors)
                sleep()
                break

            if errors >= MAX_ERRORS:
                display_hangman(errors)
                print(f"Game Over! A palavra era '{keyword}'.")
                sleep()
                print(f"Vitória de {challenger}!")
                sleep()
                break

        # reiniciar ou sair
        if input("Jogar de novo? (s/n): ").strip().lower() != "s":
            break
        clear()

if __name__ == "__main__":
    main()
