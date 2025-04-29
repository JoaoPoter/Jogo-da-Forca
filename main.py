import os
os.system("cls")

while True:
    desafiante = input("Nome do Desafiante: ")
    competidor = input("Nome do Competidor: ")
    erro = 0
    os.system("cls")

    palavra = input("Palavra chave: ")
    dica1 = input("dica1: ")
    dica2 = input("dica2: ")
    dica3 = input("dica3: ")
    dica = dica1
    os.system("cls")

    asterisks = '*' * len(palavra)
    print(f"palavra: {asterisks}")

        tentativa = input("Digite uma letra ou 'dica' para pedir uma dica: ")
        if tentativa == 'dica':
        print(f"Dica: {dica}")
    tentativa = input("Digite uma letra ou 'dica' para pedir uma dica: ")