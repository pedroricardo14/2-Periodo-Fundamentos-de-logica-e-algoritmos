lista =  ["leite", "café", "chá", "água", "refrigerante"]
try:
  opcao = int(input("Digite um número de 0 a 4: "))
  print("Você escolheu:",lista[opcao])
except IndexError:
  print("ERRO. Essa opção/posição não existe.")
except ValueError:
  print("ERRO. O valor digitado não é aceito.")
