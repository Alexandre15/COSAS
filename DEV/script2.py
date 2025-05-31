import pandas as pd
import plotly.express as px

# Lendo os dados do arquivo Excel
# Substitua 'data.xlsx' pelo caminho do seu arquivo Excel
df = pd.read_excel('C:/Users/e0616587/COSAS/DEV/data.xlsx')

# Verifique se as colunas existem
print(df.columns)

# Armazenando os valores e os nomes das categorias
# Substitua 'Results' e 'Category' pelos nomes reais das suas colunas
values = df['Results']
names = df['Category']

# Criando o gráfico de pizza
figure = px.pie(df, values=values, names=names, title='Resultados da Pesquisa')

# Atualizando as informações do gráfico
figure.update_traces(textposition='inside', textinfo='percent+label')

# Atualizando o layout do gráfico
figure.update_layout(title_font_size=24)

# Exibindo o gráfico
figure.show()

# Salvando o gráfico em um arquivo HTML
figure.write_html('Piechart.html')