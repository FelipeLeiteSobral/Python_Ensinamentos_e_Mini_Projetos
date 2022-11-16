lista_produtos = ["ÃBC001", "abc012", " ABC111", "AVb022"]


def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return (texto)


for i, produto in enumerate(lista_produtos):
    lista_produtos[i] = tratar_texto(produto)
print(lista_produtos)