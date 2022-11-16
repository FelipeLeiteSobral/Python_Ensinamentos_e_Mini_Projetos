# read para arquivos simples (ex:senhas, tokens , informações unicas)
with open("email.txt", "r") as arquivo:  # r para ler, w para rescrever ou editar, a para adicionar
    email = arquivo.read()
print(email)

senha = 123456
with open("senha.txt", "r") as arquivo:
    senha = arquivo.read()

with open("email.txt", "r") as arquivo:  # abrindo no modo leitura para fazer a edição
    email = arquivo.write("123456")
print(email)

# write para editar informações no arquivo
with open("senha.txt", "r") as arquivo:  # modo write
    senha = arquivo.write("654321")
print(senha)

# readlines para arquivos maiores

# r para ler, w para rescrever ou editar, a para adicionar
with open("email.txt", "r") as arquivo:
    email = arquivo.readlines()
print(email)
for linha in email:
    if "palavra" in linha:  # irá mostrar apenas a linha com determinada informação
        print(linha)
