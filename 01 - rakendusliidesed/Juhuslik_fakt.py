import requests
from easygui import *  
aadress = "https://cat-fact.herokuapp.com/facts/random" 
päring = requests.get(aadress)
andmed = päring.json()
valikud =["jah", "ei"]
answer = buttonbox("Would you like to know something interesting?", choices = valikud)
if answer == "jah":
    msgbox(andmed['text'])
else:
    msgbox("Kurb lugu.")
    msgbox(andmed['text'])