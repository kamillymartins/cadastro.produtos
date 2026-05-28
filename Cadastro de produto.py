import os

produtos = []
inicio = 1


while(inicio == 1):
    print("-----MENU DE CADASTRO-----")
    print("1 - Adicionar produto.")
    print("2 - Listar produtos")
    print("3 - Sair")
    print("--------------------------")

    opcao = float(input("Escolha o que vai fazer:"))

    if(opcao == 1):
        nome = input("Digite o nome do produto: " )
        produtos.append(nome)
        

    elif(opcao ==2):
        for produto2 in produtos:
            print(produto2)

    elif opcao == "3":
        break # Quebra o loop e encerra o programa


