import requests
from datetime import datetime
import os
from colorama import Fore, Style, init

init(autoreset=True)

numverify_key = ("b82a9f21278d466c5251a0f384ce432b")
abstract_key = ("cea4b8ce437d453c968fe48390a5976e")


def scan(phone):
    print(Fore.CYAN + "\n========== PHONE OSINT ELITE ==========\n")

    hasil = {}

    # ======================
    # API 1 : Numverify
    # ======================
    if numverify_key:
        try:
            url = f"https://api.apilayer.com/numverify/validate?number={phone}"
            headers = {"apikey": numverify_key}
            res = requests.get(url, headers=headers, timeout=10)
            data = res.json()

            if data.get("valid"):
                hasil = {
                    "Valid": data.get("valid"),
                    "Nomor": data.get("international_format"),
                    "Negara": data.get("country_name"),
                    "Kode Negara": data.get("country_code"),
                    "Lokasi": data.get("location") or "Tidak tersedia",
                    "Operator": data.get("carrier") or "Tidak tersedia",
                    "Tipe Line": data.get("line_type") or "Tidak tersedia",
                    "Sumber": "Numverify"
                }
        except:
            pass

    # ======================
    # API 2 : AbstractAPI
    # ======================
    if not hasil and abstract_key:
        try:
            url = f"https://phonevalidation.abstractapi.com/v1/?api_key={abstract_key}&phone={phone}"
            data = requests.get(url, timeout=10).json()

            if data.get("valid"):
                hasil = {
                    "Valid": data.get("valid"),
                    "Nomor": data.get("format", {}).get("international"),
                    "Negara": data.get("country", {}).get("name"),
                    "Kode Negara": data.get("country", {}).get("code"),
                    "Lokasi": data.get("location") or "Tidak tersedia",
                    "Operator": data.get("carrier") or "Tidak tersedia",
                    "Tipe Line": data.get("type") or "Tidak tersedia",
                    "Sumber": "AbstractAPI"
                }
        except:
            pass

    if not hasil:
        print(Fore.RED + "\nGagal mendapatkan data dari semua API\n")
        return None

    print(Fore.GREEN + "\n========== HASIL ==========\n")

    for k, v in hasil.items():
        print(Fore.YELLOW + f"{k:<15}: " + Fore.WHITE + f"{v}")

    # ======================
    # SAVE REPORT
    # ======================
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_file = f"reports/phone_{phone}_{timestamp}.txt"
    html_file = f"reports/phone_{phone}_{timestamp}.html"

    with open(txt_file, "w") as f:
        for k, v in hasil.items():
            f.write(f"{k}: {v}\n")

    with open(html_file, "w") as f:
        f.write("<html><body><h2>PHONE OSINT REPORT</h2><table border='1'>")
        for k, v in hasil.items():
            f.write(f"<tr><td>{k}</td><td>{v}</td></tr>")
        f.write("</table></body></html>")

    print(Fore.CYAN + f"\nReport TXT  : {txt_file}")
    print(Fore.CYAN + f"Report HTML : {html_file}")

    return hasil

