#Eu sei que isso não faz parte do exercício. Eu só tava feliz de ter conseguido fazer esse código e queria salvá-lo em algum lugar.

num = int(input("Digite o número aqui:"))
divisores = 0

for divisor in range(1, num):   
    if num % divisor == 0:  
        divisores = divisores + 1
        if divisores > 1:   
            break

if divisores > 1:   
    print("Este número não é primo.")
elif num == 1:  
    print("Caso especial. Você digitou o número um.")
elif num == 0:  
    print("Caso especial. Você digitou o número zero.")
elif num < 0:   
    print("Caso especial. Você digitou um número negativo.")
else:   
    print("Este número é primo.")
