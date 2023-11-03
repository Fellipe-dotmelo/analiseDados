import pandas as pd

vendas_DF = pd.read_excel("Groupby.xlsx")

print("\n DataFrame Vendas \n")
print(vendas_DF)
print("\n")

#groupby - Agrupas pela coluna de Vendedor e usando o mean para calcula a média
mediaVendedor = vendas_DF.groupby(["Vendedor"]).mean(numeric_only=True)

print("\n groupby - Agrupas pela coluna de Vendedor e usando o mean para calcula a média \n")
print(mediaVendedor)
print("\n")

somaVendedor = vendas_DF.groupby(["Vendedor"]).sum(numeric_only=True)
print("\n groupby - Agrupas pela coluna de Vendedor e usando o sum calcula a soma \n")
print(somaVendedor)
print("\n")

#--------
#groupby = agrupa pela coluna
#dropna = deleta linhas se houver um valor ou mais em branco
#by = usa a coluna selecionada como critério para fazer o groupby
#sum = soma
MantendoValoresBrancos = vendas_DF.groupby(by=["Vendedor"], dropna=False).sum(numeric_only=True)
print("\n Agrupa pela coluna vendeodor e considera por valores em branco \n")
print(MantendoValoresBrancos)
print("\n")

#groupby = agrupa pela coluna
#dropna = deleta linhas se houver um valor ou mais em branco
#by = usa a coluna selecionada como critério para fazer o groupby
#sum = soma
RemovendoValoresBrancos = vendas_DF.groupby(by=["Vendedor"], dropna=True).sum(numeric_only=True)
print("\n Agrupa pela coluna vendedor e remove linhas com os valores em branco \n")
print(RemovendoValoresBrancos)
print("\n")

#--------
agrupaDuasColunas = vendas_DF.groupby(["Vendedor", "Produto"]).sum(numeric_only=True)
print("\n Agrupa pelas colunas de vendedor e Produto fazendo soma dos valores \n")
print(agrupaDuasColunas)
print("\n")

agrupaProdutosVendedor = vendas_DF.groupby(["Produto", "Vendedor"]).sum(numeric_only=True)
print("\n Agrupa pelas colunas de Produto e Vendedor fazendo soma dos valores \n")
print(agrupaProdutosVendedor)
print("\n")

agrupaDataVendedor = vendas_DF.groupby(["Data Venda", "Vendedor"]).sum(numeric_only=True)
print("\n Agrupa pelas colunas de Data da venda e Vendedor tambem faz a soma dos valores \n")
print(agrupaDataVendedor)
print("\n")