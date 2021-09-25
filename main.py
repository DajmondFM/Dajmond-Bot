import discord
from discord.ext import commands, tasks
from discord_slash import SlashCommand
import random
import os
from dotenv import load_dotenv

client = commands.Bot(command_prefix="$")
v = "v0.01"
uk = "Użyto komendy "
client.remove_command("help")
slash = SlashCommand(client, sync_commands=True)


@client.event 
async def on_ready():
  print("Zalogowaliśmy się do {0.user}".format(client))
  print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   █▀▄ ▄▀█ ░░█ █▀▄▀█ █▀█ █▄░█ █▀▄\n▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   █▄▀ █▀█ █▄█ █░▀░█ █▄█ █░▀█ █▄▀")

@slash.slash(description="Pokazuje opóźnienie jakie ma bot")
async def js(ctx):
  print(uk + "/Ping")
  await ctx.send(f"Pong {round(client.latency * 1000)}ms")

@client.command(name="ping")
async def ping(ctx):
  print(uk + "Ping")  
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

load_dotenv()
TOKEN = os.getenv("Token")
client.run(TOKEN)