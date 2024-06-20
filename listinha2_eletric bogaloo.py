comidas = ['leite', 'couve','computador', 'tomate','garfo','faca','tablet','refrigerante']
bebidas = ['uva', 'colher','TV','vinho','cerveja','celular','banana']
talheres = ['arroz','iPhone', 'concha','whisky','vodka','feijão','colher de chá']
eletronicos = []

comidas.remove ("leite")
comidas.remove ("computador")
comidas.remove ("garfo")
comidas.remove ("faca")
comidas.remove ("tablet")
comidas.remove ("refrigerante")

bebidas.remove ("uva")
bebidas.remove ("colher")
bebidas.remove ("TV")
bebidas.remove ("celular")
bebidas.remove ("banana")

talheres.remove ("arroz")
talheres.remove ("iPhone")
talheres.remove ("whisky")
talheres.remove ("vodka")
talheres.remove ("feijão")

comidas.extend (["uva", "banana", "arroz", "feijão"])
bebidas.extend (["leite", "refrigerante", "whisky", "vodka"])
talheres.extend (["garfo", "faca", "colher"])
eletronicos.extend (["computador", "tablet", "TV", "celular", "iPhone"])

print ("Comidas:", comidas)
print ("Bebidas:", bebidas)
print ("Talheres:", talheres)
print ("Eletrônicos:", eletronicos)
