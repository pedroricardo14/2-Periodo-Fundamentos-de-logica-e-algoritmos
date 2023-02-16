#6.Crie uma função que recebe um número e diz se ele é primo.

def primo(numero):
  divisores = 0
  for x in range(1, numero+1):
    resto = numero % x 
    if resto == 0:
      divisores = divisores + 1
  ### FIM DO FOR #################
  if divisores <= 2:
    print(f"{numero} É PRIMO!")
  else:
    print(f"{numero} não é primo. Ele tem {divisores} divisores.")

primo(75)
