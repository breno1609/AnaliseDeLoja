import pandas as pd

# Análise da Base de Dados
tabela = pd.read_excel("Vendas.xlsx")
# Faturamento Total
faturamento_total = tabela["Valor Final"].sum()
# Faturamento por Loja
faturamento_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
# Faturamento por Produto
faturamento_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_produto)