import os
import random
import threading
import time
import tkinter as tk

# Base path to the downloaded fake system directory
FAKE_BASE = os.path.expanduser("~/Downloads/system_root")

# Actions to simulate on the fake files
ACTIONS = [
    ("[🗑️] Deleting file: {}", os.remove),
    ("[☣️] Corrupting file: {}", lambda f: open(f, "w").write("💀 VIRUS INJECTION 💀")),
    ("[🔐] Encrypting file: {}", lambda f: open(f, "w").write("ENCRYPTED_DATA_BLOCK"))
]

def find_all_files(base_dir):
    all_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files

def simulate_destruction(text_widget):
    files = find_all_files(FAKE_BASE)
    random.shuffle(files)

    start_time = time.time()
    duration = 30  

    while time.time() - start_time < duration and files:
        file = files.pop()
        message_template, action = random.choice(ACTIONS)
        try:
            action(file)
            message = message_template.format(file)
        except Exception as e:
            message = f"[!] Failed on {file}: {e}"
        text_widget.insert(tk.END, message + "\n")
        text_widget.see(tk.END)
        time.sleep(random.uniform(0.2, 0.4))
    text_widget.insert(tk.END, "\n\n💀 SYSTEM DAMAGED BEYOND RECOVERY 💀", "end")
    text_widget.see(tk.END)
    time.sleep(4)

    # Final touch - Restart the machine (requires sudo)
    exit_code = os.system("reboot")
    print(f"Exit Code: {exit_code}")



def start_ui():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.bind("<Escape>", lambda e: root.destroy())

    text = tk.Text(root, bg="black", fg="lime", font=("Courier", 14), borderwidth=0)
    text.pack(expand=True, fill="both")
    text.config(cursor="none")
    text.tag_config("end", foreground="red", font=("Courier", 22, "bold"))

    threading.Thread(target=simulate_destruction, args=(text,), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    start_ui()
