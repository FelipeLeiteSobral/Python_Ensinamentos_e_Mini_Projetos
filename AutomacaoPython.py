import pandas as pd
import win32com.client as win32

# importar a base de dados
tabela_vendas = pd.read_excel("Vendas.xlsx")

# Visualizar base de dados
pd.set_option("display.max_columns", None)
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby(
    "ID Loja").sum()
print(faturamento)

# quantidade de produtos vendidos por loja

quantidade = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade)

print("-" * 50)

# ticket medio por produto em cada loja
ticket_medio = (faturamento["Valor Final"]/quantidade["Quantidade"]).to_frame()
ticket_medio = ticket_medio.rename(columns={0: "Ticket Médio"})
print(ticket_medio)

# enviar um email com o relatorio
outlook = win32.Dispatch("outlook.application")
email = outlook.CreatItem(0)
mail.To = "felipeleitesobral@hotmail.com"
mail.Subject = "Relatório de Vendas por loja"
mail.HTMLBody = f'''
<p> Prezados, </p>

<p> Segue o Relatório de Vendas por cada Loja. </p>
