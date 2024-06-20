num = int(input("Digite o número aqui:"))
soma = 0
divisor = 1

while divisor < num:    
    if num % divisor == 0:  
        soma = soma + divisor
        divisor = divisor + 1
    else:   
        divisor = divisor + 1

if num == soma: 
    print ("Este é um número perfeito.")
else:   
    print ("Este não é um número perfeito.")
    
