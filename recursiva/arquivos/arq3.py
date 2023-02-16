# 1
"""numeros = list(range(9, 75, 14))
print(numeros)"""


#2
"""numeros = list(range(351, 712, 45))
print(numeros)"""

#3
"""lancamento = list(range(10, 0, -1))
print(lancamento)"""

#4
"""lista = ["Pedro", "Maeldson", "Nicassio", "Davi"]
for nome in lista:
    print(f"Bom dia,{nome}!")"""

#5



"""contador=0
for c in range(1,80, 5):
    contador+=5
    print(f"Senhas de {contador} a {contador+5}:____________")"""


#6

def passageiros(qnt):
    if qnt == 1:
        print("Recomendamos usar uma motocicleta.")
    elif 1<=qnt<=4:
        print("Recomendamos usar um automovel.")
    elif 4<=qnt<=8:
        print("Recomendamos usar uma minivan.")
    elif 8<=qnt<=14:
        print("Recomendamos usar uma van")
    elif 14<=qnt<=20:
        print("Recomendamos usar um micro-onibus")
    elif 20<=qnt<=50:
        print("Recomendamos usar um onibus")
    else:
        print("Digite um numero entre 1 e 50: ")
        
passageiros(6)









