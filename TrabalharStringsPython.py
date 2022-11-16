from statistics import mean


variavel1 = 54
variavel2 = 54.0
variavel3 = "Batata"
print(type(variavel1))
print(type(variavel2))
print(type(variavel3))
print(variavel3)

# numero de vezes para troca de strings
variavel3_trocada = variavel3.replace("a", "x", 1)
variavel3_trocada1 = variavel3_trocada.casefold()
print(variavel3_trocada1)

# verificar se letras sao todas maiusculas
print(variavel3_trocada1.isupper())

# verificar se letras sao todas minusculas
print(variavel3_trocada1.islower())

# verificar se string é numerico
cpf = "213.121.323-19"
print(cpf.isnumeric())

# verificar se string tem somente letras
print(cpf.isalpha())

# verificar se string tem somente numeros e letras
print(cpf.isalnum())

# Repetição de letras numa string
for letra in variavel3_trocada1:
    print(letra)

notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mean(notas))
