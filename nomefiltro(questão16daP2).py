nomes = ["Miguel", "Sohpia", "Davi", "Alice", "Arthur", "Julia", "Pedro", "Isabella", "Gabriel", "Manuela", "Bernardo", "Laura", "Lucas", "Luiza", "Matheus", "Valentina", "Rafael", "Giovana", "Heitor", "Maria Eduarda"]
letra = str(input("Digite UMA letra:"))
letra = letra.upper()

filtro = filter(lambda nome: nome.startswith(letra), nomes)

print (list(filtro))
