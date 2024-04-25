num = float(input("Digite o número aqui: "))

if num % 2 == 0 and num > 0:    
    print("Este número é positivo e par.")
elif num > 0 and num % 3 == 0:  
    print("Este número é positivo e múltiplo de três.")
elif num < 0 and num % 2 != 0: 
    print("Este número é negativo e ímpar.")
elif num == 0:  
    print("Este número é zero.")
else: 
    print("Este número não corresponde a nenhuma das categorias testadas.")
