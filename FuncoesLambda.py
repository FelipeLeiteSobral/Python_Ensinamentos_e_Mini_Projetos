# Expressões Lmabda (Funções anonimas)- Simplificado / nao tem nome
preco = 1000


def calcular_imposto(preco):
    return preco * 0.3


print(calcular_imposto(preco))


precos = [500, 300, 150, 10]
impostos = list(map(lambda x: x/10, precos))
print(impostos)

lista_filmes = ["a", " b", " c ", " D"]
def ajeitar_texto(x): return x.upper() and x.strip()


print(list(map(ajeitar_texto, lista_filmes)))
