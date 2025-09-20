import tkinter as tk
import random
import time
import threading
import os

fake_logs = [
    "[    0.000000] Initializing cgroup subsys cpuset",
    "[    0.000000] Linux version 5.11.0-41-generic (buildd@lcy01-amd64-018)",
    "[    0.123456] CPU: Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz",
    "[    0.234567] Kernel panic - not syncing: Fatal exception",
    "[    0.345678] CPU: 0 PID: 1 Comm: swapper/0 Not tainted",
    "[    0.456789] Call Trace: <IRQ>",
    "[    0.567890] RIP: 0010:__bad_area_nosemaphore+0x13c/0x200",
    "[    0.678901] CR2: 0000000000000000",
    "[    0.789012] ---[ end Kernel panic - not syncing: Fatal exception ]---",
    "[    0.890123] BUG: unable to handle kernel NULL pointer dereference",
    "[    1.012345] Oops: 0000 [#1] SMP NOPTI",
    "[    1.123456] Modules linked in: overlay",
    "[    1.234567] panic: segmentation fault at address 0x0",
    "[    1.345678] Hardware name: FakeLinux 5.11 crash-x86_64 GNU/Linux",
    "[    1.456789] systemd[1]: Failed to start Journal Service.",
    "[    1.567890] systemd[1]: Dependency failed for Initrd Root File System.",
    "[    1.678901] systemd[1]: Dependency failed for Reload Configuration from the Real Root.",
    "[    1.789012] Rebooting in 60 seconds...",
    "[    1.890123] [CRITICAL] System integrity check failed.",
    "[    2.000000] *** SYSTEM HALTED ***"
]

boot_cmds = [
    "dmesg | tail -n 20",
    "journalctl -xe",
    "cat /var/log/syslog | tail -n 10"
]

colors = ['black', 'darkred', 'purple', 'black', 'maroon']
user = "sahib"
host = "linux"

def show_fake_crash():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.bind("<Escape>", lambda e: root.destroy())

    text = tk.Text(root, bg="black", fg="white", font=("Courier", 14), borderwidth=0)
    text.pack(expand=True, fill="both")
    text.config(cursor="none")
    text.tag_config("end", foreground="red", font=("Courier", 26))

    def flicker_bg():
        for _ in range(30):
            root.configure(bg=random.choice(colors))
            time.sleep(0.15)
        root.configure(bg="black")

    def type_commands():
        for cmd in boot_cmds:
            prompt = f"{user}@{host}:~$ "
            for char in prompt + cmd:
                text.insert(tk.END, char)
                text.see(tk.END)
                root.update()
                time.sleep(0.03)
            text.insert(tk.END, "\n[!] System log corruption detected.\n\n")
            text.see(tk.END)
            time.sleep(0.5)

    def type_logs():
        start_time = time.time()
        while time.time() - start_time < 20:
            line = random.choice(fake_logs)
            text.insert(tk.END, f"{line}\n")
            text.see(tk.END)
            time.sleep(0.15)

        text.insert(tk.END, "\n\n\n\n\n      SYSTEM DESTROYED.. GOOD BYE, HUMAN\n", "end")
        text.see(tk.END)
        time.sleep(2)

        text.see(tk.END)

    threading.Thread(target=flicker_bg, daemon=True).start()
    threading.Thread(target=type_commands, daemon=True).start()
    threading.Thread(target=type_logs, daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    show_fake_crash()
