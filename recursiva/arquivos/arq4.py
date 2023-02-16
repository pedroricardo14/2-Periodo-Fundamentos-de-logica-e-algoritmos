"""Crie um programa de cadastro que armazena as informações em uma lista. O programa deve permitir adicionar, listar e remover
itens na lista. O programa deve gravar a lista em um arquivo e recuperar as informações sempre que for necessario"""

dados = [] # lista vazia

while True:
    print("== MENU ==")
    print("1 Cadastrar")
    print("2 Listar")
    print("3 Remover")
    opcao = input("Opção? ")
    
    if opcao == "1":
        dados.append(input("Digite um item: "))
        print("Item adicionado.")
    elif opcao == "2":
        for item in dados:
            print(item)
    elif opcao == "3":
        item = input("Item a ser removido: ")
        if item in dados:
            dados.remove(item)
            print("Item removido.")
            
    arq = open("lista.txt", "w")
    for item in dados:
        arq.write(item+"\n")
    arq.close()
    
