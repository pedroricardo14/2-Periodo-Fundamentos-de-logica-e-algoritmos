#4.Crie uma função que recebe um número entre 1 e 7 e imprime o dia da semana. Considere: 1/domingo, 2/segunda, 3/terça... 7/sábado. Se o valor não estiver no intervalo, informar que é inválido.  diadasemana(3)

def diadasemana(dia):
  if dia == 1:
    print("Domingo")
  elif dia == 2:
    print("Segunda-feira")
  elif dia == 3:
    print("Terça-feira")
  elif dia == 4:
    print("Quarta-feira")
  elif dia == 5:
    print("Quinta-feira")
  elif dia == 6:
    print("Sexta-feira")
  elif dia == 7:
    print("Sábado")
  else:
    print("Dia inválido")

####### PROGRAMA PRINCIPAL ##########
diadasemana(1)
