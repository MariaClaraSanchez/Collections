# Conjunto (set)
Um conjunto no Python é representado por vários elementos, que não possuem repetição.


# Se a ordem de entrada não importa, posso usar de cara já o conjunto(set)
    usuarios_data_science = {15, 23, 43, 56}
    usuarios_machine_learning = {13, 23, 56, 42}

# Um conjuto é mutavel, ou seja posso inserir e remover elementos dentro dele.

Mas é possível congelar o conjunto, e deixar ele imutavel:
    frozenset(usuario)

# defaultdict
Se tenho uma função, seja o construtor de um objeto ou uma função qualquer, essa função vai ser chamada toda vez que o defaultdict falhar na busca, falhar na chave, buscar a chave e não achar essa chave.