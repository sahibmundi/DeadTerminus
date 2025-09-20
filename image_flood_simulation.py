import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import time
import threading

IMAGE_FOLDER = "images"  
IMAGE_DURATION = 2 

def start_image_loop():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.bind("<Escape>", lambda e: root.destroy())

    label = tk.Label(root, bg="black")
    label.pack(expand=True)
    label.config(cursor="none")

    image_files = [os.path.join(IMAGE_FOLDER, f)
                   for f in os.listdir(IMAGE_FOLDER)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    if not image_files:
        print("No images found in folder.")
        return

    def loop_images():
        while True:
            img_path = random.choice(image_files)
            img = Image.open(img_path)

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)


            tk_img = ImageTk.PhotoImage(img)
            label.config(image=tk_img)
            label.image = tk_img  # Prevent garbage collection

            time.sleep(IMAGE_DURATION)

    threading.Thread(target=loop_images, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    start_image_loop()
