peso = float(input("Digite o seu peso em Kg: "))
altura = float(input("Digite a sua altura em m: "))
imc = (peso / (altura ** 2))
print(imc)
if imc >= 40:    
    print("Obesidade grave.")
elif imc >= 30: 
    print("Obesidade.")
elif imc >= 25: 
    print("Sobrepeso.")
elif imc >= 18.5:   
    print("Valor ideal.")
elif imc >= 17: 
    print("Magreza leve.")
elif imc >= 16: 
    print("Magreza moderada.")
else:   
    print("Magreza grave.")
