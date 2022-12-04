# Array
import array as arr

arr.array('d', [])

# Desempacotar 
usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando
  print(nome)

for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)


# Operator
from operator import attrgetter
from src.classes.contaSalario import ContaSalario

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]


for conta in sorted(contas, key=attrgetter("_saldo")):
  print(conta)



