import os
from venv import create
from IPython.display import display
from pathlib import Path
import pandas as pd

# Irá mostrar o seu arquivo está localixado em seu computador
caminho = Path.cwd()
print(caminho)

tabelas_vendas = pd.DataFrame(
    columns=["Loja", "Vendedor", "Valor da Venda"])  # informar colunas
# acessar todos os arquivos da pasta selecionada
for pasta in caminho.iterdir():
    if pasta.is_dir():
        # chdir = change directory (mudar de diretório) - entrar nas pastas existentes
        os.chdir(pasta)
        caminho = Path.cwd()
        for pasta in caminho.iterdir():
            if pasta.is_dir():
                os.chdir(pasta)
                caminho = Path.cwd()
                for pasta in caminho.iterdir():
                    if pasta.is_dir():
                        os.chdir(pasta)
                        caminho = Path.cwd()
                        for pasta in caminho.iterdir():
                            if pasta.is_dir():
                                os.chdir(pasta)
                                caminho = Path.cwd()
                                for pasta in caminho.iterdir():  # acesso a todas as pastas
                                    if pasta.is_dir():
                                        os.chdir(pasta)
                                        caminho = Path.cwd()
                                        for arquivo in caminho.iterdir():  # leitura de cada arquivo dentro de cada pasta
                                            tabela_vendas = pd.read_excel(
                                                arquivo)
                                            tabelas_vendas = tabelas_vendas.append(
                                                tabela_vendas, ignore_index=True)  # Juntar todas as listas em uma só
vendas_agregado = tabelas_vendas.groupby(
    by="Loja").sum()  # somar as vendas das cidades
del vendas_agregado["Vendedor"]
display(vendas_agregado)

# Define o diretorio a ser selecionado (pasta a ser selecionada)
os.chdir(r'C:\Users\Abílio\Desktop\Formulário\python\continuação\Vendas')
print(Path.cwd())
vendas_agregado.to_excel("Vendas Agragadas por Loja.xlsx")
