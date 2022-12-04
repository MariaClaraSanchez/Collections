# Array

O array serve justamente ter uma eficácia maior quando estivermos trabalhando principalmente com números.

O array do Python tem um tipo específico. Pois para criar um array no Python, eu tenho que falar o tipo e todos os elementos têm que ser desse tipo.


No dia a dia usual do Python usa-se as listas. 
Em situações específicas, onde se tem um conjunto bem pequeno de elementos onde cada posição indica uma coisa, é comum usar as tuplas. 
E onde é muito importante se ter um alto desempenho de funções matemáticas, é muito comum usar a biblioteca a numpy.

Então por isso os Arrays, acabam por não serem muito utilizados

# isinstance()

A função isinstance() retorna True se o objeto especificado for do tipo especificado, caso contrário, False .

# Ordenar do menor para o maior

    sorted(lista)

# Ordenar do maior para o menor
Retorna uma lista:

    sorted(lista, reverse=True) 

Reverse, não retorna uma lista:

    reversed()

# Operator

https://docs.python.org/pt-br/3/library/operator.html


# attrgetter()

No attrgetter(), eu posso falar o critério de desempate.


    for conta in sorted(contas, key=attrgett ("_saldo""_codigo")):
        print(conta)


