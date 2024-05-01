import pandas as pd
from tabulate import tabulate

# Carregar o arquivo CSV
df = pd.read_csv("main-data.csv")

# Filtrar os dados onde language_type é igual a "markup"
programming_df = df[df['language_type'] == 'markup']

# Calcular a média para cada linguagem de marcação
media_por_linguagem = programming_df.groupby('language')['num_pushers'].mean()

# Encontrar as 20 maiores médias
maiores_medias = media_por_linguagem.nlargest(20)

# Criar uma lista de tuplas com os dados para a tabela
tabela_dados = [(linguagem, media) for linguagem, media in maiores_medias.items()]

# Criar uma tabela formatada
tabela_formatada = tabulate(tabela_dados, headers=['Linguagem', 'Média de pushers'], tablefmt='grid')

# Imprimir a tabela formatada
print(tabela_formatada)
