from textos import textos
from collections import Counter

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

if __name__ == "__main__":
    texto1,texto2 = textos()
    print("Texto 1:\n")
    analisa_frequencia_de_letras(texto1)
    print("\n*****************************\n")
    print("Texto 2:\n")
    analisa_frequencia_de_letras(texto2)
    print()