# importando o pandas
from IPython.display import display
from numpy import disp
import pandas as pd

# Criando um dataframe a partir de um dicionario
# dataframe = pd.DataFrame()

venda = {"data": ["15/02/2021", "16/02/2021"],
         "valor": [500, 300],
         "produto": ["feijão", "arroz"],
         "qtde": [50, 70],
         }
print(venda)
# Data frame seria uma tabela
tabelas_vendas = pd.DataFrame(venda)
display(tabelas_vendas)

# Importando arquivos e bases de dados

tabelas_vendas = pd.read_excel("Vendas.xlsx")
# Entrega apenas os 5 primeiros itens
display(tabelas_vendas.head())
# Entrega o numero de linhas e o numero de colunas
display(tabelas_vendas.shape)
# Entrega parametros de métricas
display(tabelas_vendas.describe())

# pegar apenas 1 coluna ou colunas selecionadas (e os pd.Series)

produtos = tabelas_vendas[["Produto", "ID Loja"]]
display(produtos)

# pegar linhas (.loc) - baseado no índice (pd.Series)

display(tabelas_vendas.loc[1])

# fazer comparações e condições (pegar apenas um item em comum numa unica linha ou unica coluna)
vendas_norte_shopping_df = tabelas_vendas.loc[tabelas_vendas["ID Loja"]
                                              == "Norte Shopping"]

# fazer varias comparações entre linhas e colunas
vendas_norte_shopping_df_comparacoes = tabelas_vendas.loc[tabelas_vendas["ID Loja"] == "Norte Shopping", [
    "ID Loja", "Produto", "Quantidade"]]
display(vendas_norte_shopping_df_comparacoes)

# pegar 1 valor especifico
print(tabelas_vendas.loc[1, "Produto"])

# Adicionar 1 coluna ou linha

tabelas_vendas["Comissão"] = tabelas_vendas["Valor Final"] * 0.05
display(tabelas_vendas["Comissão"])

# Criar uma coluna com valor padrão

tabelas_vendas.loc[:, "Imposto"] = 0
display(tabelas_vendas.head())

tabelas_vendas_dez = pd.read_excel("Vendas - Dez.xlsx")
display(tabelas_vendas_dez)

# adicionar tabela de dezembra à tabela padrão
tabelas_vendas = tabelas_vendas.append(tabelas_vendas_dez)
display(tabelas_vendas)

# Excluir linhas ou colunas (drop(ponto, eixo-horizontal"1"/vertical"0")
tabelas_vendas = tabelas_vendas.drop("Imposto", axis=1)

# Deletar linhas ou colunas vazias
# exclui a coluna onde tiver valor vazio
tabelas_vendas = tabelas_vendas.dropna(how="all", axis=1)
# exclui linhas onde tem pelo menos 1 valor vazio
tabelas_vendas = tabelas_vendas.dropna()

# preencher valores vazios
tabelas_vendas["Comissão"] = tabelas_vendas["Comissão"].fillna(
    5)  # preenche valores vazios com o numero 5

# preencher com o ultimo valor (mesclar linhas/colunas do excel)
tabelas_vendas = tabelas_vendas.ffill()

# Indicadores
# contagem de aparições do item numa coluna ou numa linha
transacoes_loja = tabelas_vendas["ID Loja"].value_counts
# junta item semelhante e soma as informações desse item
faturamento_produto = tabelas_vendas.groupby("Produto").sum()

# Mesclar 2 dataframes (procurar informações de um dataframe em outro)
gerentes_df = pd.read_excel("Gerentes.xlsx")
display(gerentes_df)
# Identifica colunas com mesmo nome, verifica itens em interseccao e adiciona a uma tabela
tabelas_vendas = tabelas_vendas.merge(gerentes_df)
display(tabelas_vendas)
