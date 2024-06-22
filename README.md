# FocusDetectorV3
Colaborades: Vinicius de Oliveira Chapula, Lucas Cavalheiro, Angelika Andreatta

Para rodar o projeto e validar o dataset ele estara disponivel no arquivo zip "DataSetsUtilizados.zip"

# Explicação da estrutura de pastas e arquivos

DataSet: Pasta onde esta localizada a base de imagens utilizada para o treinamento  <br>
OrganizarDataSet.py: Script utlizado para separar em pasta as classes para termos uma noção melhor do dataset <br>
RenomearDataset.py: Script utilizado para renomear as imagens para padronização e organização do dataset <br>
ContarDataset.py: Script utilizado para contar a quantidade de imagens em cada classe <br>
Runs: Pasta aonde se fica o resultado do treinamento <br>
config.yaml: Nele setamos aonde esta localizado as imagens de treino, validação e treinamento para que o modelo possa identificar <br>
train.ipynb: Script de treinamento nele passamos os pesos iniciais para deste e o arquivo de config <br>
BestV1.pt: Pesos feitos antes do tratamento das imagens apenas a base bruta sem passar por refinamento <br>
BestV2.pt: Pesos gerados apóa o refinamento e tratamento do dataset <br>
focusdetectorv2.py: FrontEnd para utilização dos pesos gerados no treinamento nele basta você inserir na mão qual peso você deseja utilizar, por padrão deixamos como o bestV2.pt <br>
resultados: Onde fica salvo as predições feita pelo modelo <br>
