import os
from ultralytics import YOLO
import cv2
from tkinter import Tk, filedialog, Button, Label

# Instale as bibliotecas necessárias
#!pip install ultralytics opencv-python-headless

# Função para selecionar arquivo
def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(title="Selecione um arquivo", filetypes=[("Arquivos JPG", "*.jpg"), ("Arquivos MP4", "*.mp4")])
    return arquivo

# Função para detectar objetos
def detectar_objetos(arquivo, modelo, pasta_saida):
    extensao = os.path.splitext(arquivo)[1].lower()
    confianca_minima = 0.7  # Definimos a confiança mínima como 70%
    
    if extensao in ['.jpg', '.jpeg', '.png']:
        imagem = cv2.imread(arquivo)
        resultados = modelo(imagem)
        for resultado in resultados:
            boxes = resultado.boxes
            # Filtrar detecções pela confiança mínima
            boxes = [box for box in boxes if box.conf > confianca_minima]
            # Atualizar boxes no resultado
            resultado.boxes = boxes
            # Salvar o resultado
            nome_arquivo_saida = os.path.join(pasta_saida, "resultado_" + os.path.basename(arquivo))
            cv2.imwrite(nome_arquivo_saida, resultado.plot())
        
    elif extensao in ['.mp4', '.avi', '.mov']:
        cap = cv2.VideoCapture(arquivo)
        quatrocc = cv2.VideoWriter_fourcc(*'mp4v')
        nome_arquivo_saida = os.path.join(pasta_saida, "resultado_" + os.path.basename(arquivo))
        out = cv2.VideoWriter(nome_arquivo_saida, quatrocc, 20.0, (int(cap.get(3)), int(cap.get(4))))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            resultados = modelo(frame)
            for resultado in resultados:
                boxes = resultado.boxes
                # Filtrar detecções pela confiança mínima
                boxes = [box for box in boxes if box.conf > confianca_minima]
                # Atualizar boxes no resultado
                resultado.boxes = boxes
                frame = resultado.plot()
            out.write(frame)
        
        cap.release()
        out.release()
    else:
        raise ValueError("Formato de arquivo não suportado. Selecione um arquivo JPG ou MP4.")

# Função para o botão de seleção de arquivo
def acao_botao():
    arquivo = selecionar_arquivo()
    if not arquivo:
        label_resultado.config(text="Nenhum arquivo selecionado.")
        return
    
    modelo = YOLO("bestV2.pt")
    
    pasta_saida = "resultados"
    os.makedirs(pasta_saida, exist_ok=True)
    
    detectar_objetos(arquivo, modelo, pasta_saida)
    label_resultado.config(text=f"Arquivo salvo em: {os.path.abspath(pasta_saida)}")

# Interface Gráfica
root = Tk()
root.title("Detecção de Objetos com YOLO")

label_instrucoes = Label(root, text="Clique no botão abaixo para selecionar um arquivo JPG ou MP4:")
label_instrucoes.pack(pady=10)

botao_selecionar = Button(root, text="Selecionar Arquivo", command=acao_botao)
botao_selecionar.pack(pady=10)

label_resultado = Label(root, text="")
label_resultado.pack(pady=10)

root.mainloop()
