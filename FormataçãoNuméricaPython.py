faturamento = 1500
custo = 500
lucro = faturamento - custo
# A virgula faz separação de milhar e o .2f informa 2 casas decimais
print(f"O lucro foi de R${lucro:,.2f}")
margem = lucro/faturamento
print(f"A margem foi de {margem:.1%}")
# O .1% colocará em percentual
texto_lucro = f"R${lucro:_.2f}"
texto_lucro = texto_lucro.replace(".", ",").replace("_", ".")
# Trocar ponto por vírgula e vírgula por ponto
print(f"O lucro foi de {texto_lucro}")
