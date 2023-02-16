try:
  numero = int(input("Digite um numero: "))
  print("Você digitou:", numero)
except ValueError:
  print("Erro. O valor digitado é inválido")
finally:
  print("Chegamos ao fim do programa! :)")
