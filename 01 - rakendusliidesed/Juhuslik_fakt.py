import requests
from easygui import *
def huvitav_fakt(aadress):
    päring = requests.get(aadress)
    andmed = päring.json()
    msgbox(andmed['text'])
aadress = "https://cat-fact.herokuapp.com/facts/random" 
valikud =["jah", "ei"]
valik = ["jah, tahan veel ühte","ei, aitab küll"]
kordus = 1
i = 0
Esimene_kord = True
while i < kordus:
    answer = buttonbox("Kas tahad teada midagi huvitavat?", choices = valikud)
    if answer == "jah":
        huvitav_fakt(aadress)
        answer = buttonbox("Tahad veel ühte fakti?", choices = valik)
        Esimene_kord = False
        if answer == "jah, tahan veel ühte":
            huvitav_fakt(aadress)             
        else:
            msgbox("Kena päeva!")
            break
    elif Esimene_kord == True:
        msgbox("Kurb lugu. Saad ikka teada.")
        huvitav_fakt(aadress)
        break
    else:
        msgbox("Kena päeva!")
        break
