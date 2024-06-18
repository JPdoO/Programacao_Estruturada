num = int(input("Digite no número de termos que deseja ver na sequência:"))

ultimo = 1
penultimo = 0

if num == 0:    
    print (0)
elif num == 1:  
    print (1)
else:   
    for contador in range (0, num): 
        termo = ultimo + penultimo 
        penultimo = ultimo 
        ultimo = termo 
        contador = contador + 1

print (termo)