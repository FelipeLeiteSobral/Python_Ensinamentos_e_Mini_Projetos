import openpyxl
import pandas as pd
from IPython.display import display
tabela = pd.read_excel(
    r"C:\Users\Abílio\Desktop\Formulário\python\continuacao\Vendas.xlsx")
display(tabela)

# para somar mais colunas coloca-se mais um colchete ([])
# para agrupar a coluna usa-se o groupby
faturamento_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
# display(faturamento_loja)

# para agrupar mais de uma coluna coloca-se colchetes([])
faturamento_produto_loja = tabela[["ID Loja", "Valor Final", "Produto"]].groupby(
    ["ID Loja", "Produto"]).sum()
display(faturamento_produto_loja)
