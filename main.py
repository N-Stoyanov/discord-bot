import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

#To secure the token code 
load_dotenv()

#Actual Bot Code
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN is None:
    print("Error: DISCORD_BOT_TOKEN not found in .env file.")
    exit()

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

    # Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hi there {ctx.author.mention}!")

# Command: !shutdown
@bot.command()
async def shutdown(ctx):
    await ctx.send("Shutting down...")
    await bot.close()

@bot.command()
async def roll(ctx):
    number = random.randint(1,6)
    await ctx.send(f"{ctx.author.mention} rolled a {number}!")

@bot.event
async def on_reaction_add(reaction, user):
    if user != bot.user:
        await reaction.message.channel.send(f"{user.mention} reacted with {reaction.emoji}")

bot.run(TOKEN)

