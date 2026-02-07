import requests

target = input("Masukkan IP / Domain: ")
url = f"http://ip-api.com/json/{target}"

data = requests.get(url).json()

for k,v in data.items():
    print(f"{k} : {v}")
