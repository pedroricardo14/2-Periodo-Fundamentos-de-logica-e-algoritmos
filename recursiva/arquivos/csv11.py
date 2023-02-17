try:
    arquivo = open("lista.txt","r") # r - leitura
    print(arquivo.read())
    #dados = arquivo.read()
    #print(dados)
    #arquivo.write("Besouro")
    arquivo.close()

except FileNotFoundError:
    print("Arquivo não existe.")
    
except:
    print("Erro ao ler arquivo.")
