import discord
from discord import client
from discord.ext import commands, tasks
# from discord_slash import SlashCommand
import random
import os

client = commands.Bot(command_prefix="$")
v = "v0.01"
client.remove_command("help")
# slash = SlashCommand(client, sync_commands=True)


@client.event 
async def on_ready():
  print("Zalogowaliśmy się do {0.user}".format(client))
  print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   █▀▄ ▄▀█ ░░█ █▀▄▀█ █▀█ █▄░█ █▀▄\n▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   █▄▀ █▀█ █▄█ █░▀░█ █▄█ █░▀█ █▄▀")

my_secret = os.environ['Token']
client.run(my_secret)