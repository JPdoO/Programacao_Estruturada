num = int(input("Digite o número:"))
fator = 1

for produto in range (1, num + 1):  
    fator *= produto 

print ("O resultado do fatorial de %d é igual a %d" % (num, fator))
