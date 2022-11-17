# É básicamente uma tabela, onde são separados por dois pontos (:)
# KEYS é o primeiro valor e o segundo é VALUES
emails_gerentes = {
    "Iguatemi": "iguatemi@gmail.com",
    "Plaza": "plaza@gmail.com",
    "Barra": "barra@gmail.com"
}

# Mostrar o correspondente do item especificado
email = emails_gerentes["Iguatemi"]
print(email)
for shopping in emails_gerentes.values():
    print(shopping)

# Exclui a correlação a partir da KEY
emails_gerentes.pop("Barra")
print(emails_gerentes)

# Verificar se tem item dentro do dicionario
if "iguatemi@gmail.com" in emails_gerentes.values():
    print(True)
else:
    print(False)
