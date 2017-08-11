print("Bem vindo ao espaco aluno")
alunos = []
nota1 = []
nota2 = []
nota3 = []
quantidade = int(raw_input("Digite a quantidade de alunos: \n"))
i = 1

while i <= quantidade:
	alunos.append(raw_input("Aluno %i:" %i))
	nota1.append (int (raw_input("Nota 1:")))
	nota2.append (int(raw_input("Nota 2:")))
	nota3.append (int(raw_input("Nota 3:")))
	i += 1

j = 0
print ("NOTA DOS ALUNOS : \n")
while j < quantidade:
	media = float ((nota1[j] + nota2[j] + nota3[j]) / 3)
	if media >= 6:
		 status = "Aprovado"
	else:
		status = "Reprovado"
	print ("Nome %s - Status %s \n Nota 1: %d \n Nota 2: %d       Media : %d \n Nota 3: %d" %(alunos[j],status,nota1[j],nota2[j], media,nota3[j]))
	j+= 1
