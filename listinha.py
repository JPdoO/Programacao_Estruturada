lista = []

for presença in range (1, 15):  
    nome = str(input("Digite o nome do aluno (digite a palavra fim para quando não houver mais alunos presentes):"))
    lista.append (nome)
    if nome == "fim":    
        break

print ("Os alunos presentes são: ", lista)
