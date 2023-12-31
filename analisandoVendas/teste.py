from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Especifique o nome do arquivo Excel
vendasProdutos = "vendas_dados atual.xlsx"

# Crie um DataFrame vazio para armazenar os dados mesclados
dados_mesclados = pd.DataFrame()

# Lista com os nomes das abas/sheets que você deseja mesclar
dias_do_mes = range(1, 31)
abas = [f'dia{dia}' for dia in dias_do_mes]

# Inicializar a lista para armazenar os DataFrames
dataframes = []

# Itere sobre as abas e leia cada uma delas, adicionando à lista apenas se a aba existir
for aba in abas:
    try:
        df = pd.read_excel(vendasProdutos, sheet_name=aba)
        dataframes.append(df)
    except pd.errors.ParserError:
        pass  # Ignorar a aba se ela não existir

# Se a lista de DataFrames não estiver vazia, concatene-os
if dataframes:
    dados_mesclados = pd.concat(dataframes, ignore_index=True)
else:
    dados_mesclados = pd.DataFrame()

# Combine as colunas 'Item' e 'Forma de Pagamento' em uma nova coluna chamada 'Item_Forma_Pagamento'
dados_mesclados['Item_Forma_Pagamento'] = dados_mesclados['Item'] + " - " + dados_mesclados['Forma de Pagamento']

# Calcular a quantidade de itens vendidos
quantidade_itens_vendidos = dados_mesclados['Quantidade'].sum()

# Calcular os itens vendidos
itens_vendidos = dados_mesclados['Item'].unique()

# Calcular os valores de cada item
valores_por_item = dados_mesclados.groupby('Item')['Valor'].sum()

# Calcular o total arrecadado
total_arrecadado = dados_mesclados['Valor'].sum()

# Calcular o valor arrecadado por 'Água' e 'Gás'
valor_arrecadado_agua = round(valores_por_item.get('Água', 0), -2)
valor_arrecadado_gas = round(valores_por_item.get('Gás', 0), -2)
valor_arrecadado_gasBotijao = round(valores_por_item.get('Gás com Botijão', 0), -2)


# Cores personalizadas para 'Água' e 'Gás'
cores_personalizadas = {
    'Água': 'blue',
    'Gás': 'yellow',
    'Gás com Botijão': 'gray',
}

# Crie um gráfico de barras para visualizar os valores por item com a quantidade
plt.figure(figsize=(10, 6))
bars = plt.bar(valores_por_item.index, valores_por_item.values, color=[cores_personalizadas.get(item, 'lightgray') for item in valores_por_item.index])

# Adicionar rótulos de quantidade nas barras
for bar, quantidade in zip(bars, dados_mesclados.groupby('Item')['Quantidade'].sum()):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(quantidade), ha='center', va='bottom')

# Inclua as informações de valor arrecadado no título
def formatar_titulo_com_moeda(titulo, simbolo_moeda, valor_arrecadado_agua, valor_arrecadado_gas):
    return titulo.format(simbolo_moeda, valor_arrecadado_agua, simbolo_moeda, valor_arrecadado_gas)

titulo_grafico = f"Valores por Item - Quantidade Total: {quantidade_itens_vendidos}\nÁgua - arrecadou: {valor_arrecadado_agua} R$\n Gás - arrecadou: {valor_arrecadado_gas} R$\n  Gás com Botijão - arrecadou: {valor_arrecadado_gasBotijao} R$\n"
plt.title(titulo_grafico)
plt.xlabel("Item")
plt.ylabel("Valor (R$)")
plt.xticks(rotation=0)

# Legenda com quadrados coloridos para cada item
legend_elements = [Patch(facecolor=cor, label=item) for item, cor in cores_personalizadas.items()]
plt.legend(handles=legend_elements, loc='upper left')

img_path = "marca-dagua-2.png"
img = plt.imread(img_path)
imagebox = OffsetImage(img, zoom=0.060, resample=True, clip_path=None, clip_box=None, alpha=0.5)
ab = AnnotationBbox(imagebox, (0, 1.090), frameon=False, xycoords='axes fraction', boxcoords="axes fraction")
plt.gca().add_artist(ab)

plt.show()

