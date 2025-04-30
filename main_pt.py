import os
import time
from hangman import display_hangman

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    desafiante = input("Desafiante, digite seu nome: ").strip()
    competidor = input("Competidor, digite seu nome: ").strip()

    limpar_tela()
    palavra_secreta = input("Desafiante, digite a palavra secreta: ").strip().lower()
    dicas = [input(f"Dica {i + 1}: ").strip() for i in range(3)]

    letras_tentadas = []
    palavra_oculta = '*' * len(palavra_secreta)
    erros = 0
    dica_usada = False
    indice_dica = 0

    while True:
        limpar_tela()
        print(f"Palavra escolhida por {desafiante}: {palavra_oculta}")
        print(f"Letras tentadas: {', '.join(letras_tentadas) or 'Nenhuma'}")
        display_hangman(erros)

        prompt = f"{competidor}, tente uma letra, a palavra"
        if not dica_usada and indice_dica < len(dicas):
            prompt += f" ou digite 'dica' para a dica {indice_dica + 1}: "
        else:
            prompt += ": "
        tentativa = input(prompt).strip().lower()

        if tentativa == "dica":
            if not dica_usada and indice_dica < len(dicas):
                print(f"Dica {indice_dica + 1}: {dicas[indice_dica]}")
                indice_dica += 1
                dica_usada = True
            elif indice_dica >= len(dicas):
                print("Não há mais dicas disponíveis.")
            else:
                print("Você já usou a dica neste turno.")
            time.sleep(2)
            continue

        if len(tentativa) == 1 and tentativa.isalpha():
            if tentativa in letras_tentadas:
                print(f"Você já tentou a letra '{tentativa}'.")
            else:
                letras_tentadas.append(tentativa)
                dica_usada = False

                if tentativa in palavra_secreta:
                    palavra_oculta = ''.join([
                        letra if letra == tentativa or letra == palavra_oculta[i] else '*'
                        for i, letra in enumerate(palavra_secreta)
                    ])
                    print(f"Boa! A letra '{tentativa}' está na palavra.")
                    if palavra_oculta == palavra_secreta:
                        limpar_tela()
                        print(f"Parabéns, {competidor}! Você adivinhou a palavra: '{palavra_secreta}'!")
                        display_hangman(erros)
                        time.sleep(3)
                        break
                else:
                    erros += 1
                    print(f"A letra '{tentativa}' não está na palavra.")
                    if erros == 6:
                        limpar_tela()
                        display_hangman(erros)
                        print(f"Fim de jogo! A palavra era '{palavra_secreta}'. {desafiante} venceu!")
                        time.sleep(3)
                        break
            time.sleep(2)

        elif tentativa == palavra_secreta:
            limpar_tela()
            print(f"Parabéns, {competidor}! Você adivinhou a palavra: '{palavra_secreta}'!")
            display_hangman(erros)
            time.sleep(3)
            break

        else:
            print("Entrada inválida. Digite uma letra, a palavra completa ou 'dica'.")
            time.sleep(2)
