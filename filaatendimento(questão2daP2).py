fila = int(input("Digite o número de clientes na fila a princípio:"))

while fila > 0: 
    entrada = (str(input("Tem cliente chegando? (Responda com sim ou não)")))
    if entrada == "sim":  
        fila = fila + 1
        print ("A fila agora tem %d pessoas." %(fila))
    else:   
        print ("A fila continua tendo %d pessoas" %(fila))
    saida = (str(input("Algum cliente foi atendido? (Responda com sim ou não)")))
    if saida == "sim":  
        fila = fila - 1
        print ("A fila agora tem %d pessoas." %(fila))
    else:   
        print ("A fila continua tendo %d pessoas." %(fila))
