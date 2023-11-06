import pandas as pd
import matplotlib.pyplot as plt

# Especifique o nome do arquivo Excel
vendasProdutos = "vendas_dados.xlsx"

# Crie um DataFrame vazio para armazenar os dados mesclados
dados_mesclados = pd.DataFrame()

# Lista com os nomes das abas/sheets que você deseja mesclar
abas = ["dia1", "dia2", "dia3"]

# Itere sobre as abas e leia cada uma delas e concatene no DataFrame de dados_mesclados
for aba in abas:
    df = pd.read_excel(vendasProdutos, sheet_name=aba)
    dados_mesclados = pd.concat([dados_mesclados, df])

# Combine as colunas 'Item' e 'Forma de Pagamento' em uma nova coluna chamada 'Item_Forma_Pagamento'
dados_mesclados['Item_Forma_Pagamento'] = dados_mesclados['Item'] + " - " + dados_mesclados['Forma de Pagamento']

# Calcular a quantidade de itens vendidos
quantidade_itens_vendidos = dados_mesclados['QUANTIDADE'].sum()

# Calcular os itens vendidos
itens_vendidos = dados_mesclados['Item'].unique()

# Calcular os valores de cada item
valores_por_item = dados_mesclados.groupby('Item')['Valor'].sum()

# Calcular o total arrecadado
total_arrecadado = dados_mesclados['Valor'].sum()

# Imprimir as informações
print(f"Quantidade de itens vendidos: {quantidade_itens_vendidos}")
print("Itens vendidos:")
for item in itens_vendidos:
    print(f"- {item}")
print("Valores por item:")
for item, valor in valores_por_item.items():
    print(f"- {item}: R${valor:.2f}")
print(f"Total arrecadado: R${total_arrecadado:.2f}")

# Criar um gráfico de barras para visualizar os valores por item com a quantidade
plt.figure(figsize=(10, 6))
bars = plt.bar(valores_por_item.index, valores_por_item.values)

# Adicionar rótulos de quantidade nas barras
for bar, quantidade in zip(bars, dados_mesclados.groupby('Item')['QUANTIDADE'].sum()):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(quantidade), ha='center', va='bottom')

plt.title(f"Valores por Item - Quantidade Total: {quantidade_itens_vendidos}")
plt.xlabel("Item")
plt.ylabel("Valor (R$)")
plt.xticks(rotation=45)
plt.show()
