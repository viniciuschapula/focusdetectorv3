#FocusDetectorV3
Colaborades: Vinicius de Oliveira Chapula, Lucas Cavalheiro, Angelika Andreatta

Para rodar o projeto e validar o dataset ele estara disponivel no arquivo zip "DataSetsUtilizados.zip"

#Explicação da estrutura de pastas e arquivos

DataSet: Pasta onde esta localizada a base de imagens utilizada para o treinamento
OrganizarDataSet.py: Script utlizado para separar em pasta as classes para termos uma noção melhor do dataset
RenomearDataset.py: Script utilizado para renomear as imagens para padronização e organização do dataset
ContarDataset.py: Script utilizado para contar a quantidade de imagens em cada classe
Runs: Pasta aonde se fica o resultado do treinamento
config.yaml: Nele setamos aonde esta localizado as imagens de treino, validação e treinamento para que o modelo possa identificar
train.ipynb: Script de treinamento nele passamos os pesos iniciais para deste e o arquivo de config
BestV1.pt: Pesos feitos antes do tratamento das imagens apenas a base bruta sem passar por refinamento
BestV2.pt: Pesos gerados apóa o refinamento e tratamento do dataset
focusdetectorv2.py: FrontEnd para utilização dos pesos gerados no treinamento nele basta você inserir na mão qual peso você deseja utilizar, por padrão deixamos como o bestV2.pt
resultados: Onde fica salvo as predições feita pelo modelo
