import os
import time
while True:
    os.system("cls")

    contadorDicas = 0
    totalErros = 0

    desafiante = input("Nome do Desafiante: ")
    competidor = input("Nome do Competidor: ")
    os.system("cls")
    palavra = input("Palavra chave: ")
    secreta = "*" * len(palavra)
    dica1 = input("Dica 1: ")
    dica2 = input("Dica 2: ")
    dica3 = input("Dica 3: ")
    
    while True:
        os.system("cls")
        print("(1) Jogar")
        print("(2) Dica")
        print(f"A palavra secreta é: {secreta}")
        print(f"Total de Erros: {totalErros}")

        opcao = input()

        if opcao == "1":
            tentativa = input("Informe a letra: ")
            posicao = 0
            acertou = False
            secreta = list(secreta)
            for letra in palavra:
                if letra == tentativa:
                    secreta[posicao] = tentativa
                    acertou = True
                posicao += 1
            secreta = ''.join(secreta)
            if acertou == False:
                totalErros += 1
            
            if "*" not in secreta:
                print(f"O competidor {competidor} ganhou!")
                print(f"O desafiante {desafiante} perdeu!")
                time.sleep(2)
                break
            
        elif opcao == "2":
            contadorDicas += 1
            if contadorDicas == 1:
                print(f"Dica 1: {dica1}")
                time.sleep(2)
            elif contadorDicas == 2:
                print(f"Dica 2: {dica2}")
                time.sleep(2)
            elif contadorDicas == 3:
                print(f"Dica 3: {dica3}")
                time.sleep(2)
            else:
                print("Você não tem mais dicas!")
                time.sleep(2)
        else:
            print("Opção inválida!")
            time.sleep(2)
