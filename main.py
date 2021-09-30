import discord
from discord import channel
from discord.ext import commands, tasks
from discord_slash import *
from discord_buttons_plugin import  *
import random
import os
from dotenv import load_dotenv

client = commands.Bot(command_prefix="$")
v = "v0.05"
uk = "Użyto komendy "
# client.remove_command("help")
buttons = ButtonsClient(client)
slash = SlashCommand(client, sync_commands=True)


@client.event 
async def on_ready():
  await client.change_presence(activity=discord.Game("Aktualna wersja bota to " + v))
  print("Zalogowaliśmy się do {0.user}".format(client))
  print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   █▀▄ ▄▀█ ░░█ █▀▄▀█ █▀█ █▄░█ █▀▄\n▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   █▄▀ █▀█ █▄█ █░▀░█ █▄█ █░▀█ █▄▀")

@slash.slash(name="ping", description="Pokazuje opóźnienie jakie ma bot")
async def js(ctx):
  print(uk + "/Ping")
  await ctx.send(f"Pong {round(client.latency * 1000)}ms")

@slash.slash(description="TEST")
async def test(ctx):
  await ctx.send("test")

@client.command(name="ping")
async def ping(ctx):
  print(uk + "Ping")  
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def test(ctx):
  await ctx.reply("test")




# TEST
@client.command()
async def status(ctx):
  await buttons.send(
    content="Wybierz status!",
    channel=ctx.channel.id,
    components=[
      ActionRow([
        Button(
          label="Gra",
          style=ButtonType().Primary,
          custom_id="game"),
        Button(
          label="Stream",
          style=ButtonType().Primary,
          custom_id="live"),
        Button(
          label="Słuchanie muzyki",
          style=ButtonType().Primary,
          custom_id="music"),
        Button(
          label="Oglądanie YT",
          style=ButtonType().Primary,
          custom_id="film")
      ])
    ]
  )

@buttons.click
async def game(ctx):
  await client.change_presence(activity=discord.Game(name="Minecraft <3")) 
@buttons.click
async def live(ctx):
  await client.change_presence(activity=discord.Streaming(name="Life", url="https://www.twitch.tv/dajmondnull"))
@buttons.click
async def music(ctx):
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Polish Rap"))
@buttons.click
async def film(ctx):
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name="YouTube"))

load_dotenv()
TOKEN = os.getenv("Token")
client.run(TOKEN)