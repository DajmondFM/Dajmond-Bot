import discord
from discord import channel
from discord import message
from discord.ext import commands, tasks
from discord_slash import *
from discord_buttons_plugin import  *
import random
import os
from dotenv import load_dotenv
import time

client = commands.Bot(command_prefix="$")
v = "v0.07"
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
async def ping(ctx):
  print(uk + "/Ping")
  await ctx.send(f"Pong {round(client.latency * 1000)}ms")

@client.command(name="ping")
async def ping(ctx):
  print(uk + "Ping")  
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

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

@client.command()
async def nwd(ctx, cyfra1: int, cyfra2:int):
  print(uk + "NWD")
  licznik=0
  while cyfra1!=cyfra2:
    licznik+=1
    if cyfra1>cyfra2:
        cyfra1=cyfra1-cyfra2 
    else:
        cyfra2=cyfra2-cyfra1
  await ctx.send("Pętla wykonana {} razy".format(licznik))
  await ctx.send("NWD to: {}".format(cyfra1))

@client.command(aliases=['purge'])
async def cls(ctx, amount=11):
  if(not ctx.author.guild_permissions.manage_messages):
    await ctx.reply("Nie masz permisji!")
    return
  amount = amount+1
  if amount > 101:
    await ctx.reply("Nie mogę usunąć więcej niż 100 wiadomość")
  else:
    await ctx.channel.purge(limit=amount)
    await ctx.send("Wiadomości zostały usunięte!")
    time.sleep(1)
    await ctx.channel.purge(limit=1)

#test
# @client.command()
# async def test(ctx):
#   await ctx.reply("test")
#
# @slash.slash(description="TEST")
# async def test(ctx):
#   await ctx.send("test")

load_dotenv()
TOKEN = os.getenv("Token")
client.run(TOKEN)