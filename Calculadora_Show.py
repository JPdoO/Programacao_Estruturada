num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
operacao = input("Digite o sinal da operação: ")
if operacao == "+": 
    print(num1 + num2)
elif operacao == "-":   
    print(num1 - num2)
elif operacao == "*":   
    print(num1 * num2)
elif operacao == "/":   
    print(num1 / num2)
elif operacao == "**":  
    print(num1 ** num2)
else:   
    print("Erro, você não digitou um sinal de operação.")
