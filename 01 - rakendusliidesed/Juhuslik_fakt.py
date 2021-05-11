import requests
from easygui import *  
aadress = "https://cat-fact.herokuapp.com/facts/random" 
päring = requests.get(aadress)
andmed = päring.json()
valikud =["jah", "ei"]
valik = ["jah, tahan veel ühte","ei, aitab küll"]
kordus = 1
i = 0

while i < kordus:
    answer = buttonbox("Would you like to know something interesting?", choices = valikud)
    if answer == "jah":
        päring = requests.get(aadress)
        andmed = päring.json()
        msgbox(andmed['text'])
        i = i + 1
        kordus = kordus + 1
        answer = buttonbox("Tahad veel ühte fakti?", choices = valik)
        if answer == "jah, tahan veel ühte":
            päring = requests.get(aadress)
            andmed = päring.json()
            msgbox(andmed['text'])
            i = i + 1
            kordus = kordus + 1
                
        else:
            msgbox("Kena päeva!")
            break
    else:
        msgbox("Kurb lugu.")
        msgbox(andmed['text'])
        break
