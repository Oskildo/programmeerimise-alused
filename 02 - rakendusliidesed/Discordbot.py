import discord
from discord.ext import commands
from random import randint
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        print(message.author, message.channel, message.content)
        
        if message.content.lower() == "võistleme":
            await message.channel.send('olgu, vali oma rünnakut; :scissors: , :rock: or :newspaper:')
            võistlus = [":scissors:", ":rock:", ":newspaper:"]
            Roboti_valik = randint(1,3)
            if Roboti_valik == 1:
                valik = ":scissors:"
            elif Roboti_valik == 2:
                valik = ":rock:"
            else:
                valik = ":newspaper:"
            # MAke the BOt Wait
            if message.content.lower() == ":scissors:":
                võistlus = ":scissors:"
                await message.channel.send(valik)
                if võistlus == valik:
                    await message.channel.send("Viik. ")
                if valik == ":rock:":
                    await message.channel.send("Ma võitsin. :) ")
                if valik == ":newspaper:":
                    await message.channel.send("Ma kaotasin. :( ")
            elif message.content.lower(valik) == ":rock:":
                await message.channel.send(valik)
                võistlus = ":rock:"
                if võistlus == valik:
                    await message.channel.send("Viik. :( ")
                if valik == ":newspaper:":
                    await message.channel.send("Ma võitsin. :) ")
                if valik == ":scissors:":
                        await message.channel.send("Ma kaotasin. :( ")

            elif message.content.lower(valik) == ":newspaper:":
                await message.channel.send(valik)
                võistlus = ":newspaper:"
                if võistlus == valik:
                    await message.channel.send("Viik. :( ")
                if valik == ":scissors:":
                    await message.channel.send("Ma võitsin. :) ")
                if valik == ":rock:":
                        await message.channel.send("Ma kaotasin. :( ")


            elif (message.content.lower() != ":scissors:" or message.content.lower() != ":rock:" or message.content.lower() != ":rock:"):
                await message.channel.send('Sa ei mängi õigesti. Head aega.')
                
    
            

client = MyClient()
client.run("zHM3Hf2Xpe47D8sw2ls2P6yuMTHgrAYE")
