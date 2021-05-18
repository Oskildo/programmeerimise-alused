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
            while True:
                Roboti_valik = randint(1,3)
                if Roboti_valik == 1:
                    valik = ":scissors:"
                elif Roboti_valik == 2:
                    valik = ":rock:"
                else:
                    valik = ":newspaper:"
                await message.content
                if message.content.lower() == ":scissors:":
                    pass
                elif message.content.lower() == ":rock:":
                    pass
                elif message.content.lower() == ":newspaper:":
                    pass
                else:
                    await message.channel.send('Sa ei mängi õigesti. Head aega.')
                    break
    
            

client = MyClient()
client.run("ODQ0MzA3MDczODQzNDYyMTc0.YKQgPA.bD4qj5IrmiB_93UKBhisLtTq96Q")
