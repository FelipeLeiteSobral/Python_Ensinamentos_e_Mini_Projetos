from re import L
from traitlets import Undefined

# Lista ou Coluna
lista_compras = ["banana", "maca", "laranja"]
print(lista_compras)
print(lista_compras[0])

# remover item de lista
lista_compras.remove("maca")
print(lista_compras)

# remover item de lista
lista_sonhos = []
sonho = lista_compras.pop(-1)

# adicionar item na lista
lista_sonhos.append(sonho)

# adicionar item na lista em determinado indice
lista_sonhos.insert(0, "Casa")
print(lista_sonhos)

# adicão de item na lista por parte do usuario
tarefa = Undefined
lista_tarefas = []

while tarefa != "":
    tarefa = input("Insira uma tarefa ")
    lista_tarefas.append(tarefa)
    print(lista_tarefas)

# transformar listas em Tupla
lojas = ["RJ", "SP", "SE"]
faturamento = ["1000", "2000", "1200"]

# Ordenar itens do menor para o maior ou do maior para o menor
faturamento.sort(reverse=False)
print(faturamento)

resultados = []
for i in range(3):
    tupla = (lojas[i-1], faturamento[i-1])
    resultados.append(tupla)
print(resultados)

# Relacionar listas
faturamento_lojas_df = dict(zip(lojas, faturamento))
print(faturamento_lojas_df)
