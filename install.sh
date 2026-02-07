#!/data/data/com.termux/files/usr/bin/bash
pkg update -y
pkg install python git -y
pip install -r requirements.txt
chmod +x osintv5.sh

echo "Installing external tools..."
git clone https://github.com/kovinevmv/getcontact.git external/getcontact
pip install -r external/getcontact/requirements.txt

echo "[+] Install selesai"
