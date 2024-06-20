lista1 = []
contador1 = 0
lista2 = []
contador2 = 0

listacombine = []

while contador1 >= 0:   
    num1 = int(input("Digite um número para incerir na primeira lista aqui (Digite o número 0 para encerrar o processo):"))
    if num1 == 0:   
        break
    lista1.append (num1)
    contador1 = contador1 + 1

while contador2 >= 0:   
    num2 = int(input("Digite um número para incerir na segunda lista aqui (Digite o número 0 para encerrar o processo):"))
    if num2 == 0:   
        break
    lista2.append (num2)
    contador2 = contador2 + 1

listacombine.extend (lista1 + lista2)
print ("Os números da primeira lista são:", lista1)
print ("Os números da segunda lista são:", lista2)
print ("Os números das duas listas combinadas são:", listacombine)

listacombine = set (listacombine)
print ("Os números das duas listas depois de remover duplicatas são:", listacombine)
