num = float(input("Digite o valor aqui: "))
unidade = str(input("Digite a unidade de medida, entre centímetro, metro, quilômetro, polegada, pé ou milha: "))
cmtom = num / 100
cmtokm = num / 100000
cmtopolegada = num / 2.54
cmtope = num / 30.48
cmtomilha = num / 160900
mtocm = num * 100
mtokm = num / 1000
mtopolegada = num * 39.37
mtope = num * 3.281
mtomilha = num / 1609
kmtocm = num * 100000
kmtom = num * 1000
kmtopolegada = num * 39370
kmtope = num * 3281
kmtomilha = num / 1.609
polegadatocm = num * 2.54
polegadatom = num / 39.37
polegadatokm = num / 39370
polegadatope = num / 12
polegadatomilha = num / 63360
petocm = num * 30.48
petom = num / 3.281
petokm = num / 3281
petopolegada = num * 12
petomilha = num / 5280
milhatocm = num * 160900
milhatom = num * 1609
milhatokm = num * 1.609
milhatopolegada = num * 63360
milhatope = num * 5280
if unidade == "centímetro": 
    print("%f %s pode ser convertido em %f metros, %f quilômetros, %f polegadas, %f pés e %f milhas." %(num, unidade, cmtom, cmtokm, cmtopolegada, cmtope, cmtomilha))
elif unidade == "metro":    
    print("%f %s pode ser convertido em %f centímetros, %f quilômetros, %f polegadas, %f pés e %f milhas." %(num, unidade, mtocm, mtokm, mtopolegada, mtope, mtomilha))
elif unidade == "quilômetro":   
    print("%f %s pode ser convertido em %f centímetros, %f metros, %f polegadas, %f pés e %f milhas." %(num, unidade, kmtocm, kmtom, kmtopolegada, kmtope, kmtomilha))
elif unidade == "polegada": 
    print("%f %s pode ser convertido em %f centímetros, %f metros, %f quilômetros, %f pés e %f milhas." %(num, unidade, polegadatocm, polegadatom, polegadatokm, polegadatope, polegadatomilha))
elif unidade == "pé":   
    print("%f %s pode ser convertido em %f centímetros, %f metros, %f quilômetros, %f polegadas e %f milhas." %(num, unidade, petocm, petom, petokm, petopolegada, petomilha))
elif unidade == "milha":    
    print("%f %s pode ser convertido em %f centímetros, %f metros, %f quilômetros, %f polegadas e %f pés." %(num, unidade, milhatocm, milhatom, milhatokm, milhatopolegada, milhatope))
else:   
    print("Erro! Você digitou uma valor de unidade que não é válido!")
