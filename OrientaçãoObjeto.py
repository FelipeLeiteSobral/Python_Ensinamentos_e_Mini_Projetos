# Orientação Imperativa
email = "felipe@gmail.com"
arroba_local = email.find("@")
servidor = email[arroba_local + 1:]
print(servidor)

# Orientação Objeto


class Email():
    def init():
        nome = "Felipe"
        email = "felipe@gmail.com"

    def pegar_servidor():
        return email[6:]


email = Email()
print(email.pegar_servidor())
