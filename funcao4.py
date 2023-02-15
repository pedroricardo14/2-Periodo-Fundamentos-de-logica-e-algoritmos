alunos = []      #lista vazia

def cadastrar(nome):
  alunos.append(nome)

def excluir(nome):
  if nome in alunos:
    alunos.remove(nome)
    print("Removido com sucesso.")
  else:
    print("Nome não encontrado.")

def listar():
  for nome in alunos:
    print(nome)

######################################

cadastrar("Ana")
cadastrar("Felipe")
listar()
excluir("João")
excluir("Ana")
listar()
