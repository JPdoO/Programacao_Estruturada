repete = 0
soma = 0

while repete >= 0:  
    num = int(input("Digite um número à soma (Digite o número 0 para encerrar a operação):"))
    soma = soma + num
    repete = repete + 1
    if num == 0:    
        break

print ("A soma total dos números é ",soma)
