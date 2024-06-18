num = int(input("Digite o número de termos que seja maior que 0 que deseja ver na sequência:"))

ultimo = 1
penultimo = 0

lista = [0, 1]


for contador in range (0, num): 
    termo = ultimo + penultimo 
    lista.append (termo)
    penultimo = ultimo 
    ultimo = termo 
    contador = contador + 1

print (lista)
