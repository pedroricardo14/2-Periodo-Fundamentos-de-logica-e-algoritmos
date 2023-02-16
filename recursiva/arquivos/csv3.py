#arq = open("escola.csv","r")
#print(arq.read())
import csv
arq = open("escola.csv","r")
leitor = csv.reader(arq)
dados = []
for linha in leitor:
    dados.append(linha)
arq.close()

while True:
    aluno = input("Nome do aluno: ")
    serie = input("Serie: ")
    curso = input("Curso: ")
    dados.append([aluno,serie,curso])
    resp = input("Digitar outro? (s/n) ")
    if resp == "n":break

arq = open("escola.svg","w",newline="")
gravador = csv.writer(arq)
gravador.writerows(dados)
arq.close()
print("Gravado com sucesso.")
    
#print(dados)			# todos os cadastrados
#print(dados[1])			# apenas o primeiro cadastro
#print(dados[3][0])		# apenas o nome do aluno
#print(f"O aluno {dados[2][0]}, estuda {dados[2][2]}")
