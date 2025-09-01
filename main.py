import discord
import os
from dotenv import load_dotenv

#To secure the token code 
load_dotenv()

#Actual Bot Code
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')
        if message.content == "!shutdown":
            await message.channel.send("Shutting down...")
            await client.close()    
    
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)



