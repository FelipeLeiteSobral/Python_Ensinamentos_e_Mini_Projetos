# são objetos que armazenam informações (parecem-se com as listas)
# o que simboliza ser uma tupla são os parenteses()

from xmlrpc import client


tupla = (1, 2, 3, 4, 5, "Felipe")
lista = [1, 2, 3, 4, 5, "Felipe"]


print(lista[0])
print(tupla[0])


#tupla[0] = 50       - ERROR
lista[0] = 50


print(lista)
print(tupla)

# a tupla nao permite a mudança de um item especifico, uma tupla nao é mutavel (não é possivel adicionar itens tbm)

lista.append(6)
#tupla.append(6)     - ERROR

# tuplas dentro de listas
cliente = ("Felipe", "123.456.789.00", "123.456-7")
clientes = []
clientes.append(cliente)
cliente = ("Lira", "123.456.789.11", "123,456-8")
clientes.append(cliente)
print(clientes[1][0])  # indice da lista e indice da tupla

# Tuplas como chaves de dicionarios

capitais = {
    ("Brasil", "Rio de Janeiro"): ("Rio de Janeiro"),
    ("Brasil", "Sergipe"): ("Aracaju"),
    ("Brasil", "São Paulo"): ("São Paulo")
}
print(capitais.keys())
print(capitais.values())

tupla = (1, 2, 3, 4, 5, 12, 1, 2, 4, 1, 1, 1, 7)
# valor de onde tem o indice #indice de onde tem o valor # conta a quantidade de vezes que se repete algo
print(tupla[5], tupla.index(2), tupla.count(1))


lista_materiais = []


def cadastrar_materiais(nome, codigo, unidade, quantidade):
    materiais = (nome, codigo, unidade, quantidade)
    lista_materiais.append(materiais)
    return lista_materiais


def consultar_materiais(codigo):
    for materiais in lista_materiais:
        if materiais[1] == codigo:
            return print(materiais)
        else:
            pass


cadastrar_materiais("borracha", 1, "unidade", "10")
cadastrar_materiais("Tesoura", 2, "unidade", "5")
print(lista_materiais)

consultar_materiais(1)

# deletando tupla de uma lista

del lista_materiais[0]
print(lista_materiais)
