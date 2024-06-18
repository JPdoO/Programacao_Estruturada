lista = []

maior = 0
menor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

for contador in range (1, 7):   
    num = int(input("Digite o número a ser adicionado à lista:"))
    if num > maior: 
        maior = num 
        lista.append (num)
        contador = contador + 1
    if num < menor: 
        menor = num 
        lista.append (num)
        contador = contador + 1
    else:   
        lista.append (num)
        contador = contador + 1

print ("Dentre os números da lista, o maior número é %d e o menor número é %d" %(maior, menor))
