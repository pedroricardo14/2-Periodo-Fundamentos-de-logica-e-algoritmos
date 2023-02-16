#5.Crie uma função que recebe um número entre 1 e 12 e imprime o dia mês do ano. Considere: 1/janeiro, 2/fevereiro, ... 12/dezembro. Se o valor não estiver no intervalo, informar que é inválido.

def mesdoano(mes):
  if mes == 1:
    print("Janeiro")
  elif mes == 2:
    print("Fevereiro")
  elif mes == 3:
    print("Março")
  elif mes == 4:
    print("Abril")
  elif mes == 5:
    print("Maio")
  elif mes == 6:
    print("Junho")
  elif mes == 7:
    print("Julho")
  elif mes == 8:
    print("Agosto")
  elif mes == 9:
    print("Setembro")
  elif mes == 10:
    print("Outubro")
  elif mes == 11:
    print("Novembro")
  elif mes == 12:
    print("Dezembro")

  else:
    print("Mês inválido")

######## PROGRAMA PRINCIPAL ############
mesdoano(6)
