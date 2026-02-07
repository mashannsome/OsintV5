import requests

print("\nOSINT Nomor HP\n")

api_key = input("b82a9f21278d466c5251a0f384ce432b").strip()
phone = input("Nomor HP (contoh 628xxxx) : ").strip()

url = "http://apilayer.net/api/validate"

params = {
    "access_key": api_key,
    "number": phone,
    "country_code": "",
    "format": 1
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    print("\n===== HASIL =====")
    for k, v in data.items():
        print(f"{k} : {v}")

except Exception as e:
    print("Error:", e)
