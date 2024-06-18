comidas = ["leite", "couve", "tomate", "garfo", "faca", "refrigerante"]
bebidas = ["uva", "colher", "vinho", "cerveja", "banana"]
talheres = ["arroz", "concha", "whisky", "vodka", "feijão", "colher de chá"]
eletronicos = ["computador", "microondas", "geladeira", "smartphone", "videogame"]

comidas.pop (0)
comidas.pop (2)
comidas.pop (2)
comidas.pop (2)

bebidas.pop (0)
bebidas.pop (0)
bebidas.pop (2)

talheres.pop (0)
talheres.pop (1)
talheres.pop (1)
talheres.pop (1)

comidas.extend (["uva", "banana", "arroz", "feijão"])
bebidas.extend (["leite", "refrigerante", "whisky", "vodka"])
talheres.extend (["garfo", "faca", "colher"])

print ("Comidas: ", comidas)
print ("Bebidas: ", bebidas)
print ("Talheres: ", talheres)
print ("Eletrônicos: ", eletronicos)
