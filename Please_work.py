import requests
päring = requests.get("https://api.frankfurter.app/latest")
andmed= päring.json()
print(andmed)