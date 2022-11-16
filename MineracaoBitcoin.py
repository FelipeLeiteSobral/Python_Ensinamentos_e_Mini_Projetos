from hashlib import sha256
import time

# Função que vai receber um nome e assim ele será criptografado
# Hash é uma criptografia, o sha 256 pode criptografar um texto informado


def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()


def minerar(num_bloco, transacoes, hash_anterior, qtde_zeros):
    nonce = 0
    texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
    meu_hash = aplicar_sha256(texto)
    while True:  # Loop infinito, e só irá parar quando houver um return
        if meu_hash.startswith("0" * qtde_zeros):
            # função parará quando encontrar o nonce e o hash especificado para o texto
            return nonce, meu_hash
            nonce += 1


if __name__ == "__main__":  # se importar pra outro arquivo pyhon ele não excuta o que está dentro do IF
    num_bloco = 15
    transacoes = """
    Lira -> Alan -> 10
    Alan -> Joao ->5
    Joao -> Amanda -> 11"""
    qtde_zeros = 1
    hash_anterior = "abc"
    resultado = minerar(num_bloco, transacoes, hash_anterior, qtde_zeros)
    print(resultado)
