minuto = int(input("Digite a quantidade de minutos usados:"))
pulso = 0

if minuto > 400:    
    pulso = 0.15
    print ("O valor a ser pago é de R$", pulso * minuto)

elif minuto >= 200 and minuto <= 400:   
    pulso = 0.18
    print ("O valor a ser pago é de R$", pulso * minuto)

else:   
    pulso = 0.20
    print ("O valor a ser pago é de R$", pulso * minuto)
