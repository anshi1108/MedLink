import cv2
import tkinter as tk
from tkinter import ttk
from threading import Thread
from PIL import Image, ImageTk
class VideoCallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Call App")

        self.camera = cv2.VideoCapture(0)
        self.video_label = ttk.Label(root)
        self.video_label.pack()

        self.btn_mic = ttk.Button(root, text="Toggle Mic", command=self.toggle_mic)
        self.btn_mic.pack(side=tk.LEFT, padx=10)

        self.btn_camera = ttk.Button(root, text="Toggle Camera", command=self.toggle_camera)
        self.btn_camera.pack(side=tk.LEFT, padx=10)

        self.btn_end_call = ttk.Button(root, text="End Call", command=self.end_call)
        self.btn_end_call.pack(side=tk.LEFT, padx=10)

        self.mic_on = True
        self.camera_on = True
        self.update_video()

    def toggle_mic(self):
        self.mic_on = not self.mic_on
        # Add logic to handle microphone state

    def toggle_camera(self):
        self.camera_on = not self.camera_on
        # Add logic to handle camera state

    def end_call(self):
        self.root.destroy()

    def update_video(self):
        _, frame = self.camera.read()
        if self.camera_on:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            self.video_label.img = img
            self.video_label.configure(image=img)
        self.root.after(10, self.update_video)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoCallApp(root)
    root.mainloop()
