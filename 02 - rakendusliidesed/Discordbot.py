import discord
from random import randint
import asyncio
valimus = ""
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        print(message.author, message.channel, message.content)
        
        if message.content.lower() == "võistleme":
            emojis = await message.channel.send('olgu, vali oma rünnakut ehk reakti sulle saadetud emojidele.')
            await message.add_reaction("🪨")
            await message.add_reaction("✂")
            await message.add_reaction("📰")
            roboti_valik = randint(1,3)
            if roboti_valik == 1:
                valik = ":scissors:"
            elif roboti_valik == 2:
                valik = ":rock:"
            else:
                valik = ":newspaper:"
            def check(reaction, author):
                global valimus
                valimus = str(reaction.emoji)
                return author == message.author and str(reaction.emoji)

            try:
                await self.wait_for('reaction_add', timeout=20.0, check=check)
            except asyncio.TimeoutError:
                return await message.channel.send(f'Sul kestis liiga kaua aega valida.')
            await message.channel.send(valik)
            if valimus == "✂":
                võistlus = ":scissors:"
                if võistlus == valik:
                    await message.channel.send("Viik. ")
                if valik == ":rock:":
                    await message.channel.send("Ma võitsin. :) ")
                if valik == ":newspaper:":
                    await message.channel.send("Ma kaotasin. :( ")
            elif valimus == "\U0001faa8":
                võistlus = ":rock:"
                if võistlus == valik:
                    await message.channel.send("Viik. :( ")
                if valik == ":newspaper:":
                    await message.channel.send("Ma võitsin. :) ")
                if valik == ":scissors:":
                        await message.channel.send("Ma kaotasin. :( ")
            elif valimus == "📰":
                võistlus = ":newspaper:"
                if võistlus == valik:
                    await message.channel.send("Viik. :( ")
                if valik == ":scissors:":
                    await message.channel.send("Ma võitsin. :) ")
                if valik == ":rock:":
                        await message.channel.send("Ma kaotasin. :( ")
            else:
                await message.channel.send("Sa ei oska mängida. :(")
                
                
client = MyClient()
client.run("token lol")
