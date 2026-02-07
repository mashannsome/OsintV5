#!/bin/bash

pkg update -y
pkg install python git -y
pip install requests
pip install requests colorama

mkdir reports

chmod +x osintv4.sh

echo "Install selesai"
echo "Run : bash osintv4.sh"
