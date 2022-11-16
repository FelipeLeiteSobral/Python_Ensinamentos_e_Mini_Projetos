# pip install -U matplotlib (executar no terminal)
from tkinter import Label
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [1, 4, 6, 8, 1]

plt.plot(x, y, label="Dados")  # relaciona as listas
plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")
plt.title("Relação X e Y")
plt.xticks([0, 1, 2, 3, 4, 5, 6])
plt.yticks([0, 2, 4, 6, 8, 10])
# estilo de linha, cor de linha, tamanho de pontos/linhas
plt.plot(x, y, linestyle=":", color="g", lw=5.0, marker="v")
plt.scatter(x, y)  # estilo de grafico
plt.bar(x, y)  # estilo de grafico
plt.axis(xmin=-1, xmax=10, ymin=0, ymax=12)  # determinar limites do grafico
figura = plt.figure(figsize=(20, 3))
figura.suptitle("Titulo Geral")

# adicionar grafico na linha 1, com 3 colunas de grafico, posicao de coluna 1
figura.add_subplot(131)
plt.plot(x, y, label="Um dado qualquer")
plt.legend()
plt.title("Grafico1")

figura.add_subplot(132)
plt.plot(x, y, label="Um dado qualquer")
plt.legend()
plt.bar(x, y)
plt.title("Grafico1")
plt.show()  # printa o gráfico numa janela a parte
