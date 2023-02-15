# Armazenando o valor retornado pela função len numa variável
"""lista = ["café", "leite", "suco", "refri"]
qtd = len(lista)
print(qtd)"""
# Usando if
"""lista = ["café", "leite", "suco", "refri"]
if len(lista) > 2:
  print("Tem muitos elementos.")"""
#Usando index
"""lista = ["café", "leite", "suco", "refri"]
posicao = lista.index("leite")
print(posicao)"""
#Usando pop
"""lista = ["café", "leite", "suco", "refri"]
item = lista.pop(2)
print("Apaguei", item)"""

# FUNÇÃO COM RETORNO
def somar(n1, n2):
  total = n1 + n2
  return total
  #############
print(somar(7,5))

if somar(5,9) > 10:
  print("É mais de uma dezena.")

valor = somar(10,20) - somar(5,4)
print(valor)
