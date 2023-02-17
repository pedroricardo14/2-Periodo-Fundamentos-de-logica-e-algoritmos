try:
    v1 = int(input("Digite um número: "))
    v2 = int(input("Digite outro número: "))
    print("A divisão é", v1/v2)    
except ValueError:
    print("Erro na digitação.")
    
except ZeroDivisionError:
    print("Divisão por zero não aceita.")
    
except:
    print("Erro desconhecido.")
    
finally:
    print("Até a próxima")
