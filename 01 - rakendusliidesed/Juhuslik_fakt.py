import requests
from easygui import *  
aadress = "https://cat-fact.herokuapp.com/facts/random" 
päring = requests.get(aadress)
andmed = päring.json()
valikud =["jah", "ei"]
kordus = 1
i = 0

while i < kordus:
    answer = buttonbox("Would you like to know something interesting?", choices = valikud)
    if answer == "jah":
        msgbox(andmed['text'])
        i = i + 1
        kordus = kordus + 1
    else:
        msgbox("Kurb lugu.")
        msgbox(andmed['text'])
        i = i + 1
        kordus = kordus - 1 
