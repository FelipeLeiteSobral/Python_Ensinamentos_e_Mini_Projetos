# estruturas condicionais (if, elif, else) - para fazer parte da função, precisa-se estar com identação
from sre_compile import isstring
from numpy import number
from tomlkit import string
from traitlets import Undefined


nome = "Lira"
if nome == "Daniel":
    print(f"O nome dele é {nome}")
if nome == "Lira":
    print(f"O nome dele é {nome}")


# Operadores Lógicos
var1 = "parada"
var2 = 25
lista = ["Daniel", "Lira", "Candiotto", "Joao"]

if var1:  # se a var1 existe ele executará a função
    print("está preenchida")
if var2 >= 20:
    print("O valor é maior ou igual a 20")
else:
    print("O valor é menor que 20")
# se um item existe dentro de uma lista(se contem "a" em "parada")
if "a" in var1:
    print("sim")

if var1 == "parada":
    print("é String, vamos para o elif agora")
elif var2 == 5*5:  # o elif serve pra dar sequencia caso o primeiro if nao tenha sido validado a condição
    print("é Number, vamos seguir")

# condicional em uma lista
for coisa in lista:
    if coisa == "Daniel":
        print("É Daniel")
    else:
        print("Não é Daniel")


ordens = ["22001", "25464", "321344", "434435", "456345", "335446", "1223902"]

for ordem in ordens:
    if ordem[0] == "2":
        print(f"A ordem {ordem} é uma ordem preventiva")
    elif ordem[0] == "3":
        print(f"A ordem {ordem} é uma ordem corretiva")
    elif ordem[0] == "4":
        print(f"A ordem {ordem} é uma ordem preditiva")
    else:
        print(f"A ordem {ordem} é uma ordem inválida")
