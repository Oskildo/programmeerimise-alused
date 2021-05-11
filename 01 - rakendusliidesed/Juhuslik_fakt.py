import requests
aadress = "https://cat-fact.herokuapp.com/facts/random" 
päring = requests.get(aadress)
andmed = päring.json()
print(andmed['text'])