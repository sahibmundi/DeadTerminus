import tkinter as tk
import random
import threading
import time
import os

bios_cmds = [
    "sudo flashrom --programmer internal -r backup.rom",
    "efibootmgr --create --disk /dev/sda --part 1 --label 'VirusBoot'",
    "sudo dd if=/dev/zero of=/dev/sda bs=512 count=1",
    "grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=HACKED",
    "sudo nvram -c",
    "modprobe efivarfs",
    "echo '[!] BIOS LOCK BYPASSED SUCCESSFULLY'",
    "flashrom --programmer internal -w corrupted_firmware.bin",
    "rm -rf /boot/*",
    "echo '[!] Firmware injection successful...'",
]

colors = ["black", "darkred", "black", "maroon", "black"]

def show_bios_override():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.bind("<Escape>", lambda e: root.destroy())

    text = tk.Text(root, bg="black", fg="red", font=("Courier", 14), borderwidth=0)
    text.pack(expand=True, fill="both")
    text.config(cursor="none")
    text.tag_config("end", foreground="red", font=("Courier", 24))

    def flicker_bg():
        for _ in range(20):
            root.configure(bg=random.choice(colors))
            time.sleep(0.15)
        root.configure(bg="black")

    def simulate_bios_hack():
        user = "root"
        host = "localhost"
        for cmd in bios_cmds:
            prompt = f"{user}@{host}:~# "
            for char in prompt + cmd:
                text.insert(tk.END, char)
                text.see(tk.END)
                root.update()
                time.sleep(0.025)
            text.insert(tk.END, "\n")
            text.see(tk.END)
            time.sleep(0.4)
        os.system("whoami")

        time.sleep(1)
        text.insert(tk.END, "\n\n\n[!] BIOS REGION UNLOCKED — WRITING BOOT SECTOR...\n", "end")
        text.insert(tk.END, "\n[!] PERMANENT DAMAGE IN PROGRESS...\n", "end")
        text.insert(tk.END, "\n[💀] System irreversibly corrupted. Goodbye.\n", "end")
        text.see(tk.END)

    threading.Thread(target=flicker_bg, daemon=True).start()
    threading.Thread(target=simulate_bios_hack, daemon=True).start()
    root.mainloop()

if __name__ == "__main__":
    show_bios_override()
