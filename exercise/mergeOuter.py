import pandas as pd

vendasLoja1_DF = pd.read_excel("Outer_Vendas_Loja1.xlsx")
print("\n vendas loja 1: \n")
print(vendasLoja1_DF)

vendasLoja2_DF = pd.read_excel("Outer_Vendas_Loja2.xlsx")
print("\n vendas loja 2: \n")
print(vendasLoja2_DF)

#how = como fazer
#on = qual coluna puxar
#suffixes = apelidos
verificandoVendas_DF = pd.merge(vendasLoja1_DF, vendasLoja2_DF, on=["Id Vendedor"], how="outer", suffixes=("Loja 1", "Loja 2"))
print("\n Juntando Dados com Outer e verificando vendedores que venderam em ambas as lojas \n")
print(verificandoVendas_DF)

#dropna = deleta linhas com pelo menos 1 valor vazio
tratandoDados_DF = verificandoVendas_DF.dropna()
print("\n Removendo linhas com valor vazio. \n")
print(tratandoDados_DF)

del tratandoDados_DF["VendedorLoja 2"]
print("\n Removendo a coluna Vendedor Loja 2. \n")
print(tratandoDados_DF)