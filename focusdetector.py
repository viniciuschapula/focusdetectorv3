import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO
import os
import cv2

class FocusDetector:
    def __init__(self, path):
        self.model = YOLO("bestV2.pt")  # Assumindo que você tenha um modelo treinado chamado "best.pt"
        self.path = path
        self.path_save = os.path.join("results", os.path.basename(path))

    def process_image(self):
        results = self.model(self.path)
        for r in results:
            r.save(self.path_save)

    def process_video(self):
        cap = cv2.VideoCapture(self.path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))

        out = cv2.VideoWriter(self.path_save, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = self.model(frame)
            result_frame = results.render()  # Get the processed frame
            out.write(result_frame)

        cap.release()
        out.release()

    def detect(self):
        if self.path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            self.process_image()
        elif self.path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            self.process_video()

class ImageSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image/Video Selector")

        self.label = tk.Label(root, text="Selecione uma imagem ou vídeo")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Selecionar arquivo", command=self.select_file)
        self.select_button.pack(pady=10)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image and video files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif;*.mp4;*.avi;*.mov;*.mkv")])
        if file_path:
            self.show_file(file_path)

    def show_file(self, file_path):
        detector = FocusDetector(file_path)
        detector.detect()

        if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            image = Image.open(detector.path_save)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to avoid garbage collection
        elif file_path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            self.play_video(detector.path_save)

    def play_video(self, video_path):
        os.system(f'start {video_path}')  # Opens the video with the default system viewer

if __name__ == "__main__":
    if not os.path.exists("results"):
        os.makedirs("results")

    root = tk.Tk()
    app = ImageSelectorApp(root)
    root.mainloop()