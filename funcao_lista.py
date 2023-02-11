# crie uma função que recebe uma LISTA e retorna a quantidade de elementos da lista, SEM USAR A FUNÇÃO LEN 

def contar(lista):
  contador = 0
  for item in lista:
    contador = contador + 1 
  return contador

### PROGRAMA PRINCIPAL ###

materias = ["fisica", "quimica", "matemática", "história", "português", "biologia", "inglês",]
