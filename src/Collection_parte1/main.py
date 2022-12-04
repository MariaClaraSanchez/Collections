# Numpy
import numpy as np

numeros = np.array([1,3.5])

# Posso somar números no meu array
# numeros + 3 

idades = [15,87,32,65,56,32,49,37]
for i in range(len(idades)):
    print(i,idades[i])

#enumerate
for i in enumerate(idades):
    print(i)

for indice, idade in enumerate(idades):
    print(indice, idade)

# lista com os dados
# Ele cria uma lista de tuplas
list(enumerate(idades))

print()

