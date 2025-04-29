import os
import time
from hangman import display_hangman  # Certifique-se de que esta função está traduzida também

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    desafiante = input("Desafiante, digite seu nome: ").strip()
    competidor = input("Competidor, digite seu nome: ").strip()
    erros = 0
    limpar_tela()

    palavra_secreta = input("Desafiante, digite a palavra secreta: ").strip().lower()
    dicas = [input("Dica 1"),input("Dica 2"), input("Dica 3")]
    indice_dica = 0
    dica_usada = False
    letras_tentadas = []

    palavra_oculta = '*' * len(palavra_secreta)

    while True:
        limpar_tela()
        print(f"Palavra escolhida por {desafiante}: {palavra_oculta}")
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")
        display_hangman(erros)

        if not dica_usada and indice_dica < len(dicas):
            tentativa = input(f"{competidor}, tente uma letra, a palavra ou digite 'dica' para ver a dica {indice_dica + 1}: ").lower()
        else:
            tentativa = input(f"{competidor}, tente uma letra ou a palavra: ").lower()

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
                print(f"Você já tentou a letra '{tentativa}'. Tente outra.")
                time.sleep(2)
                continue

            letras_tentadas.append(tentativa)
            dica_usada = False  # Libera a dica novamente na próxima tentativa

            if tentativa in palavra_secreta:
                print(f"Boa, {competidor}! A letra '{tentativa}' está na palavra.")
                palavra_oculta = ''.join([
                    letra if letra == tentativa or letra == palavra_oculta[i] else '*'
                    for i, letra in enumerate(palavra_secreta)
                ])
                time.sleep(2)

                if palavra_oculta == palavra_secreta:
                    limpar_tela()
                    print(f"Parabéns, {competidor}! Você adivinhou a palavra '{palavra_secreta}'!")
                    print("E você estava por um triz da forca!")
                    display_hangman(erros)
                    time.sleep(3)
                    break
            else:
                print(f"A letra '{tentativa}' não está na palavra.")
                erros += 1
                time.sleep(2)

                if erros == 6:
                    limpar_tela()
                    display_hangman(erros)
                    print(f"Fim de jogo! A palavra era '{palavra_secreta}'.")
                    print(f"Parabéns {desafiante}, você venceu!")
                    time.sleep(3)
                    break

        elif tentativa == palavra_secreta:
            limpar_tela()
            print(f"Parabéns, {competidor}! Você adivinhou a palavra '{palavra_secreta}'!")
            print("E você estava por um triz da forca!")
            display_hangman(erros)
            time.sleep(3)
            break

        else:
            print("Entrada inválida. Digite uma letra, a palavra completa ou 'dica'.")
            time.sleep(2)
