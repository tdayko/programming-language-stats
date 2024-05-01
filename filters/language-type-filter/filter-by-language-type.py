import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("main-data.csv")

# Filtrar os dados onde language_type a tal
programming_df = df[df['language_type'] == 'markup']

# Salvar os dados filtrados em um novo arquivo CSV
programming_df.to_csv("./language-type-filter/programming.csv", index=False)

print("Dados filtrados salvos com sucesso!")
