import tkinter as tk
import subprocess
import threading
import time
import random

user = "sahib"
host = "linux"

linux_cmds = [
    "uname -a",
    "ls -la /",
    "free -h",
    "df -h",
    "uptime",
    "ps aux | head -10",
    "ip a",
    "whoami",
    "who",
    "id"
]

fake_msgs = [
    "[!] Deleting /boot...",
    "[!] System32 not found... Initiating fallback wipe.",
    "[!] User data breach detected.",
    "[!] Encrypting personal files...",
    "[!] root access granted to remote attacker.",
    "[!] Filesystem corrupted!",
    "[!] Exfiltrating sensitive data...",
    "[!] Launching crypto miner...",
    "[!] Disabling firewall...",
    "[!] Overwriting kernel...",
    "[!] Injecting malicious cron jobs...",
    "[!] Uploading your /home to the dark web...",
    "[!] Shadow user 'hacker' created.",
    "[!] System clock tampered.",
    "[!] Injecting backdoor...",
    "[!] Device UID leaked.",
    "[!] All partitions mounted as read/write.",
    "[!] Preparing ransom note..."
]

def run_command(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return output.strip()
    except subprocess.CalledProcessError:
        return f"[ERROR] Command failed: {cmd}"

def virus_simulation(text_widget, root):
    start_time = time.time()
    duration = 35

    while time.time() - start_time < duration:
        if random.random() < 0.4:
            msg = random.choice(fake_msgs)
            text_widget.insert(tk.END, msg + "\n")
            text_widget.see(tk.END)
            time.sleep(0.5)
        else:
            cmd = random.choice(linux_cmds)
            prompt = f"{user}@{host}:~$ "
            for c in prompt + cmd:
                text_widget.insert(tk.END, c)
                text_widget.see(tk.END)
                root.update()
                time.sleep(0.03) 
            text_widget.insert(tk.END, "\n")
            output = run_command(cmd)
            text_widget.insert(tk.END, output + "\n\n")
            text_widget.see(tk.END)
            time.sleep(0.6)

    text_widget.insert(tk.END, "\n[!] SYSTEM HACKED, BYE.......\n", "endmsg")
    text_widget.see(tk.END)

def on_escape(event, root):
    root.destroy()

def start_fake_virus():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.bind("<Escape>", lambda e: on_escape(e, root))

    text = tk.Text(root, bg="black", fg="lime", font=("Courier", 14), borderwidth=0)
    text.pack(expand=True, fill="both")
    text.config(cursor="none")
    text.tag_config("endmsg", foreground="red", font=("Courier", 20))

    threading.Thread(target=virus_simulation, args=(text, root), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    start_fake_virus()
