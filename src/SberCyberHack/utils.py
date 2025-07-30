import subprocess
import os


os.environ["GIGACHAT_TOKEN"] = ""

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()
