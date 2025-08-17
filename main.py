import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

TOKEN = "MTQwNjQ2Mzk0NjM3Mzk4ODQ4Mw.GiFz8j.8csGLx0NriwtaIrOjgZG8ZQnAMM4RXHenWkNps"

client.run(TOKEN)
