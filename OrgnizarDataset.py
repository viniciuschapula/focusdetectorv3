import os
import shutil

# Caminho para a pasta onde estão as imagens e os arquivos de texto
base_path = 'C:\\Users\\vinic\\Pictures\\Organizar\\dataset'

# Dicionário para mapear números de classe para nomes de pastas
class_map = {
    '0': 'Pneu_exposto',
    '1': 'Caixa_dagua',
    '2': 'Garrafa',
    '3': 'Piscina',
    '4': 'Prato_de_vaso_de_planta'
}

# Criar pastas para cada classe se não existirem
for class_name in class_map.values():
    class_dir = os.path.join(base_path, class_name)
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

# Processar cada arquivo de texto no diretório
for filename in os.listdir(base_path):
    if filename.endswith('.txt'):
        # Caminho completo para o arquivo de texto
        txt_path = os.path.join(base_path, filename)
        
        # Ler o primeiro caractere do arquivo para determinar a classe
        with open(txt_path, 'r') as file:
            class_num = file.read(1)
        
        # Verificar se o primeiro caractere é uma classe válida
        if class_num in class_map:
            class_name = class_map[class_num]
            
            # Caminho para a nova pasta da classe
            class_dir = os.path.join(base_path, class_name)
            
            # Caminho completo para a imagem e o arquivo de texto
            img_path = os.path.join(base_path, filename.replace('.txt', '.jpg')) # Supondo que as imagens são .jpg
            
            # Caminhos de destino
            new_txt_path = os.path.join(class_dir, filename)
            new_img_path = os.path.join(class_dir, os.path.basename(img_path))
            
            # Mover arquivos
            shutil.move(txt_path, new_txt_path)
            if os.path.exists(img_path):
                shutil.move(img_path, new_img_path)
            else:
                print(f"Imagem correspondente não encontrada para {filename}")
        else:
            print(f"Classe desconhecida encontrada no arquivo {filename}")

print("Organização do dataset concluída.")