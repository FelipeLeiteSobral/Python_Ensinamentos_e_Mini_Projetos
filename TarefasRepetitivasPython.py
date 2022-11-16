# loop FOR funciona especificando algo de uma variavel, lista, string...
#  for (nova variavel) in (variavel existente):
#       (nova variavel) que irá se repetir

from functools import partial
import string
from traitlets import Undefined


lojas = ["Rio de Janeiro", "Sao Paulo", "Belo Horizonte", "Curitiba"]
for loja in lojas:
    print(loja)

# Quantidade de repetições desejadas
for i in range(4):
    print(i)
    print(lojas[i])

# Repetição de indices
for letra in "Felipe":
    print(letra)


# loop WHILE determina uma condição para que continue o loop, ele nao tem a informação de tamanho para gerar um loop determinado
nome = Undefined
while nome != "":
    nome = input("Insira um nome ")
    print(nome)
