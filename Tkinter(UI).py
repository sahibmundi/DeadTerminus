import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import time
import random

MODULES = {
    "Boost Instagram Followers": "insta_liker_fake.py",
    "BIOS Override Tool": "bios_override_simulation.py",
    "Disk Optimizer": "disk_corruption.py",
    "Network Booster": "network_spam_attack.py",
    "Terminal Utilities": "linux_command_virus.py",
    "Visual Calibrator": "screen_flicker.py",
    "Security Log Analyzer": "mock_destruction.py",
    "Image Optimizer": "image_flood_simulation.py"
}

PROCESSING_STEPS = [
    "Connecting to ShadowPlague Network...",
    "Verifying Tool License...",
    "Authenticating Session...",
    "Downloading Required Packages...",
    "Preparing Tool Environment...",
    "Compiling Dependencies..."
]

def launch_actual_module(module_path):
    subprocess.Popen(["python3", module_path])

def open_installer(module_path, main_root):
    installer = tk.Toplevel()
    installer.title("Installing Tool")
    installer.geometry("500x350")
    installer.configure(bg="#1a1a1a")
    installer.resizable(False, False)

    tk.Label(installer, text="ShadowPlague Tool Installer", font=("Courier", 16, "bold"), 
             bg="#1a1a1a", fg="#00ff00").pack(pady=20)

    status_label = tk.Label(installer, text="Preparing Installation...", 
                           font=("Courier", 12), bg="#1a1a1a", fg="#00ff00")
    status_label.pack(pady=10)

    progress = ttk.Progressbar(installer, orient="horizontal", length=400, mode="determinate")
    progress.pack(pady=20)

    button_frame = tk.Frame(installer, bg="#1a1a1a")
    button_frame.pack(pady=20)

    def simulate_processing():
        for i, step in enumerate(PROCESSING_STEPS):
            status_label.config(text=step)
            progress["value"] = (i + 1) * (100 / len(PROCESSING_STEPS))
            time.sleep(random.uniform(0.7, 1.4))
        status_label.config(text="Tool ready to install. Proceed?")

        install_btn = tk.Button(button_frame, text="Install", font=("Courier", 12), 
                               bg="#006600", fg="white", width=10,
                               command=lambda: [installer.destroy(), launch_actual_module(module_path)])
        cancel_btn = tk.Button(button_frame, text="Cancel", font=("Courier", 12), 
                              bg="#660000", fg="white", width=10,
                              command=lambda: [installer.destroy(), main_root.deiconify()])
        install_btn.pack(side="left", padx=10)
        cancel_btn.pack(side="left", padx=10)

    threading.Thread(target=simulate_processing, daemon=True).start()

    main_root.withdraw()
    installer.protocol("WM_DELETE_WINDOW", lambda: None)
    installer.mainloop()

def main_ui():
    root = tk.Tk()
    root.title("ShadowPlague Control Panel")
    root.geometry("600x700")
    root.configure(bg="#121212")
    root.resizable(False, False)

    header = tk.Label(root, text="DeadTerminus™ Cyber Optimization Suite", 
                     font=("Arial", 20, "bold"), fg="#00ff00", bg="#121212")
    header.pack(pady=30)

    button_frame = tk.Frame(root, bg="#121212")
    button_frame.pack(pady=10)

    def on_enter(event, btn):
        btn.config(bg="#006600")

    def on_leave(event, btn):
        btn.config(bg="#1e1e1e")

    for tool, script in MODULES.items():
        btn = tk.Button(button_frame, text=tool, font=("Arial", 12), 
                       bg="#1e1e1e", fg="white", width=30, height=2,
                       relief="flat", borderwidth=2,
                       command=lambda s=script: open_installer(s, root))
        btn.pack(pady=8, padx=20)
        btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
        btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

    status_bar = tk.Label(root, text="Status: Ready", font=("Arial", 10), 
                         bg="#1a1a1a", fg="#888888", anchor="w", relief="sunken")
    status_bar.pack(side="bottom", fill="x", pady=10, padx=10)

    tk.Label(root, text="© 2025 DEAD - TERMINUS Corp. All rights reserved.", 
             bg="#121212", fg="#666666", font=("Arial", 10)).pack(side="bottom", pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_ui()