# Importação de bibliotecas
from re import X
import pandas as pd
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACa0373db7ae581055d4cdb88cce4c0bad"
# Your Auth Token from twilio.com/console
auth_token  = "f52a33f5c5d993c81f3cd5b052fc979e"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em excel
lista_meses = ["janeiro", "fevereiro", "março", "maio", "junho"] #cada arquivo salvo na pasta é uma string

for mes in lista_meses:
    tabela_vendas = pd.read_excel(mes + ".xlsx")
    if (tabela_vendas["Vendas"] > 55000).any(): # o any extende acondição para toda a coluna de vendas
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0] # o loc localiza o ponto da coluna ou da linha 
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0] # o values lhe entrega o valor no lugar de uma informação tabelada
        print("No mês de " + mes + " alguem bateu a meta. Vendedor: " + vendedor + ", Vendas: ", vendas)
        message = client.messages.create(
            to="+5579996448384", 
            from_="+12182741128",
            body=f"No mês de {mes} alguem bateu a meta. Vendedor:  {vendedor}, Vendas: {vendas}")
        print(message.sid)
# Para cada arquivo do excel procurar um valor acima de 55000 reais na coluna de vendas

# Se for maior que 55000 -> envia um SMS com o nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55000 -> fazer nada