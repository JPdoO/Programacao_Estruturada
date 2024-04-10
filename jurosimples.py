investimento = float(input("Digite o valor do investimento inicial: "))
tempo = int(input("Digite o tempo em anos: "))
taxa = int(input("Digite a porcentegem da taxa de juros: "))
jurosimples = (investimento * tempo * taxa) / 100
print("O juro simples é de ", jurosimples)
