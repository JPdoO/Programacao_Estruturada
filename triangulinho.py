lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))
if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1: 
    print("Isto não é um triângulo.")
elif lado1 == lado2 and lado1 == lado3: 
    print("Este triângulo é equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:    
    print("Este triângulo é isóceles.")
else:   
    print("Este triângulo é escaleno.")
