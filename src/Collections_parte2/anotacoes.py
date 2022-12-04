# Conjuntos:

# Criação de duas listas
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# Copiando os valores das listas para uma outra
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

# Retirando as repetições:

assistiram = set(assistiram)


# Conjunto mutavel
usuarios = {1,5,76,34,52,13,17}
usuarios.add(10)

usuario = frozenset(usuarios)

#set com strings
meu_texto = "Bem vindo meu nome é Maria eu gosto muito de nomes e tenho o meus gatos e gosto muito de gatos."
meu_texto = set(meu_texto.split())



#Dicionario
meu_texto = "Bem vindo meu nome é Maria eu gosto muito de nomes e tenho o meus gatos e gosto muito de gatos."
meu_texto = meu_texto.lower()
aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra,0)
  aparicoes[palavra] = ate_agora+1

# Dicionário de defaultdict

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1


for palavra in meu_texto.split():
  aparicoes[palavra] += 1


# Counter

from collections import Counter

aparicoes = Counter(meu_texto.split())

print(aparicoes)

print()