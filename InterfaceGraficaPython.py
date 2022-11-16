from tkinter import *
from pyparsing import col
import requests


def pegar_cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]
    texto = f"""
    Dólar: {cotacao_dolar}   
    Euro: {cotacao_euro}   
    Bitcoin: {cotacao_btc}"""

    # colocar na variavel texto_cotacoes quando for clicado o botao
    texto_cotacao["text"] = (texto)


# A criação da janela é a partir do TKINTER

janela = Tk()
janela.title("Cotação atual das moedas")  # head da pagina

# um texo se é criado por um Label
# indicar uma ordem de aparição
texto_orientacao = Label(
    janela, text="Clique no botão para aparecer a cotação das moedas")
# escolher posicao do texto a partir do GRID
texto_orientacao.grid(column=0, row=0, padx=5, pady=25)

botao = Button(janela, text="Buscar cotações do Dólar/EUR/BTC",
               command=pegar_cotacoes)  # sem parenteses para que a função nao seja rodada ja agora, seja apenas armazenada
botao.grid(column=0, row=1, padx=5, pady=25)

texto_cotacao = Label(janela, text="")
# pad e padding vao espaçar o texto
texto_cotacao.grid(column=0, row=2, padx=5, pady=25)

janela.mainloop()  # o mainloop vai fazer a janela nao fechar automaticamente
