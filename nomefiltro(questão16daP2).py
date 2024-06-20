nomes = ["Miguel", "Sohpia", "Davi", "Alice", "Arthur", "Julia", "Pedro", "Isabella", "Gabriel", "Manuela", "Bernardo", "Laura", "Lucas", "Luiza", "Matheus", "Valentina", "Rafael", "Giovana", "Heitor", "Maria Eduarda"]
letra = str(input("Digite UMA letra maiúscula:"))

filtro = filter(lambda nome: nome.startswith(letra), nomes)

print (list(filtro))
