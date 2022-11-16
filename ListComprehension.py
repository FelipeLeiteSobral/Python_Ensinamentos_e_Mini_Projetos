# objetivo do exemplo(dobrar valores e imposto de 50% de valores que possuem valor acima de 1000 reais)
# exemplo com o FOR

lista_precos = [500, 1500, 2000, 100, 25]
nova_lista_precos = []
for numero in lista_precos:
    nova_lista_precos.append(numero*2)
print(nova_lista_precos)

imposto_lista_precos = []
for numero in lista_precos:
    if numero >= 1000:
        imposto = numero*0.5
        imposto_lista_precos.append(imposto)
    else:
        imposto = 0
        imposto_lista_precos.append(imposto)
print(imposto_lista_precos)

# mesmo exemplo com LIST COMPREHENSION

# preco é a variavel a ser modificada, interagida
nova_lista_precos2 = [preco*2 for preco in lista_precos]
print(nova_lista_precos2)

imposto_lista_precos2 = [preco*0.5 if preco >=
                         1000 else 0 for preco in lista_precos]
print(imposto_lista_precos2)
