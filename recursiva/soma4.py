def soma(n):
  if n == 1:
    return 1
  else:
    return 3 + soma(n-1)

print(soma(2))
