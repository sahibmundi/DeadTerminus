import tkinter as tk
import subprocess
import threading
import random
import time

user = "sahib"
host = "linux"

linux_cmds = [
    "ping -c 1 8.8.8.8",
    "curl ifconfig.me",
    "whoami",
    "ip r",
    "ip a | grep inet | head -3",
    "ss -tuln | head -10",
    "netstat -tulpn | grep LISTEN || echo 'netstat not found'"
]


fake_ports = [
    "tcp        0      0 192.168.1.5:22      0.0.0.0:*     LISTEN     sshd",
    "tcp        0      0 192.168.1.5:80      0.0.0.0:*     LISTEN     apache2",
    "tcp        0      0 192.168.1.5:443     0.0.0.0:*     LISTEN     nginx",
    "tcp        0      0 192.168.1.5:3306    0.0.0.0:*     LISTEN     mysqld",
    "tcp        0      0 192.168.1.5:3389    0.0.0.0:*     LISTEN     rdp",
    "tcp        0      0 192.168.1.5:21      0.0.0.0:*     LISTEN     vsftpd",
    "udp        0      0 192.168.1.5:53      0.0.0.0:*     LISTEN     dnsmasq"
]

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError:
        return f"[!] Command failed: {cmd}"

def simulate_network_flood(text_widget, root):
    start_time = time.time()
    duration = 30  

    while time.time() - start_time < duration:
        if random.random() < 0.4:
            output = random.choice(fake_ports)
            text_widget.insert(tk.END, output + "\n\n")
            text_widget.see(tk.END)
            time.sleep(0.3)
        else:
            cmd = random.choice(linux_cmds)
            prompt = f"{user}@{host}:~$ "
            for char in prompt + cmd:
                text_widget.insert(tk.END, char)
                text_widget.see(tk.END)
                root.update()
                time.sleep(0.03)
            text_widget.insert(tk.END, "\n")
            output = run_cmd(cmd)
            text_widget.insert(tk.END, output + "\n\n")
            text_widget.see(tk.END)
            time.sleep(0.4)

    text_widget.insert(tk.END, "\n\n           REMOTE IPs EXFILTRATED.. SYSTEM COMPROMISED\n", "end")
    text_widget.see(tk.END)

def start_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.bind("<Escape>", lambda e: root.destroy())

    text = tk.Text(root, bg="black", fg="red", font=("Consolas", 14), borderwidth=0)
    text.pack(expand=True, fill="both")
    text.config(cursor="none")
    text.tag_config("end", foreground="red", font=("Consolas", 18))

    threading.Thread(target=simulate_network_flood, args=(text, root), daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    start_window()
