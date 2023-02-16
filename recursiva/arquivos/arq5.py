import csv

arq = open("dados1.csv", "w", newline="")

try:
    gravador = csv.writer(arq)
    gravador.writerow(["Nome", "Idade", "Sexo"])
    gravador.writerow(["Ana", "19", "F"])
    gravador.writerow(["Bruno", "23", "M"])
    gravador.writerow(["Catia", "17", "F"])
    arq.close()
    print("Gravado com sucesso.")
except:
    print("Erro gravando arquivo.")
    
