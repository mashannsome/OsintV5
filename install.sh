#!/data/data/com.termux/files/usr/bin/bash

echo "[+] Updating packages..."
pkg update -y
pkg upgrade -y

echo "[+] Installing dependencies..."
pkg install python git -y

echo "[+] Upgrading pip..."
pip install --upgrade pip

echo "[+] Installing Python requirements..."
pip install -r requirements.txt

echo "[+] Installing external tools..."
pip install maigret holehe

echo "[+] Creating folders..."
mkdir -p reports

chmod +x osintv5.sh

echo ""
echo "[+] Install selesai"
echo "[+] Jalankan dengan:"
echo "bash osintv5.sh"

