# Pegar a cotação de uma moeda em tempo real (existem API's publicas e API's privadas)
import json
import requests

# O comando GET está na página da API
cotacoes = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

# Passar um codigo em json para python
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes["USDBRL"]
cotacao_bitcoin = cotacoes["BTCBRL"]
print(cotacao_dolar["bid"])
print(cotacao_bitcoin["bid"])
