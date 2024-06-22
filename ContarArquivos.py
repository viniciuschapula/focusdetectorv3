import os

# Caminho para a pasta onde estão os arquivos
folder_path = 'dataset_full/Piscina'

# Inicializar o contador
jpg_count = 0

# Percorrer todos os arquivos na pasta
for filename in os.listdir(folder_path):
    # Verificar se o arquivo tem a extensão .jpg (case-insensitive)
    if filename.lower().endswith('.jpg'):
        jpg_count += 1

# Exibir o total de arquivos .jpg encontrados
print(f'Total de arquivos .jpg: {jpg_count}')