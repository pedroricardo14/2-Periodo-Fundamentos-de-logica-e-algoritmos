try:
  n1 = int(input("Digite um numerador: "))
  n2 = int(input("Digite o denominador: "))
  print("A divisão dá:", n1/n2)
except ValueError:
  print("ERRO. O valor digitado não é válido.")
except ZeroDivisionError:
  print("ERRO. Divisão por zero.")
  print("O denomidador não pode ser zero.")
  print("Tente novamente.")
