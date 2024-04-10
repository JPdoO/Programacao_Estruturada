precoi = float(input("Digite o valor inicial do preço: "))
desconto = int(input("Digite a porcentagem do desconto: "))
precod = precoi * desconto/100
precof = precoi - precod
if desconto > 100 or desconto <0:   
    print("ERRO! O desconto deve ser de um valor entre 0 e 100!")
elif precoi <0: 
    print("ERRO! O valor de preço não pode ser negativo!")
else:   
    print("O preço final a ser pago é de ", precof ," reais")

