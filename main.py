import pandas as pd
import re
from openpyxl import Workbook

# Definindo a expressão regular para encontrar linhas que contenham 'python'
regex_pattern = re.compile(r'.*python.*', flags=re.IGNORECASE)

# Função para filtrar as linhas do arquivo CSV com base na regex e salvar em um arquivo Excel
def filter_csv_and_save_to_excel(input_csv_file, output_excel_file):
    # Carregando o arquivo CSV para um DataFrame do pandas
    df = pd.read_csv(input_csv_file)
    
    # Aplicando a regex para filtrar as linhas
    filtered_df = df[df['language'].str.contains(regex_pattern, na=False)]
    
    # Criando um objeto ExcelWriter
    with pd.ExcelWriter(output_excel_file, engine='openpyxl') as writer:
        # Convertendo o DataFrame filtrado para um objeto de planilha do Excel
        filtered_df.to_excel(writer, index=False)
        # Fechando o objeto ExcelWriter
        writer.save()

# Caminho para o arquivo CSV de entrada e arquivo Excel de saída
input_csv_file = 'languages.csv'
output_excel_file = 'linhas_python.xlsx'

# Chamando a função para filtrar as linhas do arquivo CSV e salvar em um arquivo Excel
filter_csv_and_save_to_excel(input_csv_file, output_excel_file)

print("Linhas contendo 'python' foram filtradas e salvas em", output_excel_file)
