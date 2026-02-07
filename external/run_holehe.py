import os
import shutil

def ensure_holehe():
    if shutil.which("holehe") is None:
        print("[+] Holehe belum terinstall, installing...")
        os.system("pip install holehe")

def run(email):
    ensure_holehe()
    os.system(f"holehe {email}")
