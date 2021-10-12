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
v = "v0.09"
uk = "Użyto komendy "
client.remove_command("help")
buttons = ButtonsClient(client)
slash = SlashCommand(client, sync_commands=True)


@client.event 
async def on_ready():
  await client.change_presence(activity=discord.Game("Aktualna wersja bota to " + v))
  print("Zalogowaliśmy się do {0.user}".format(client))
  print("█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   █▀▄ ▄▀█ ░░█ █▀▄▀█ █▀█ █▄░█ █▀▄\n▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   █▄▀ █▀█ █▄█ █░▀░█ █▄█ █░▀█ █▄▀")

@slash.slash(description="Pokazuje opóźnienie jakie ma bot")
async def ping(ctx):
  print(uk + "/Ping")
  await ctx.send(f"Pong {round(client.latency * 1000)}ms")

@slash.slash(name="help", description="Pokazuje spis komend")
async def help(ctx):
  print(uk + "help")
  h = discord.Embed(title="Spis wszystkich komend!", description="Prefix bota to $", colour=0x37AEF9)
  h.add_field(name="ping", value="Pokazuje opóźnienie bota", inline=False)
  h.add_field(name="nwd", value="Oblicza NWD podanych liczb", inline=False)
  h.add_field(name="info", value="Informacje o bocie", inline=False)

  await ctx.send(embed=h)

@client.command(name="ping")
async def ping(ctx):
  print(uk + "Ping")  
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@slash.slash(name="NWD",description="Pokazuje NWD danych liczb")
async def nwd(ctx, liczba1: int, liczba2:int):
  print(uk + "NWD")
  while liczba1!=liczba2:
    if liczba1>liczba2:
        liczba1=liczba1-liczba2 
    else:
        liczba2=liczba2-liczba1
  await ctx.send("NWD to: {}".format(liczba1))

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

@slash.slash(name="info", description="Informacje o bocie")
async def info(ctx):
    info = discord.Embed(title="Informacje o bocie", description="Tutaj znajdują się najważniejsze informacje o bocie", color=0x0176BD)
    info.add_field(name="Nazwa:", value="{0.user}".format(client), inline=False)
    info.add_field(name="Autor:", value="Dajmond", inline=False)
    info.add_field(name="Wersja:", value=v, inline=False)
    info.add_field(name="GitHub:", value="https://github.com/DajmondFM/Dajmond-Bot", inline=False)
    info.add_field(name="Data stworzenia:", value="23.09.2021", inline=False )
    await ctx.send(embed=info)

#test
# @client.command()
# async def test(ctx):
#   await ctx.reply("test")
#
# @slash.slash(description="TEST")
# async def test(ctx):
#   await ctx.send("test")
#
# @client.command()
# async def nwd(ctx, cyfra1: int, cyfra2:int):
#   print(uk + "NWD")
#   licznik=0
#   while cyfra1!=cyfra2:
#     licznik+=1
#     if cyfra1>cyfra2:
#         cyfra1=cyfra1-cyfra2 
#     else:
#         cyfra2=cyfra2-cyfra1
#   await ctx.send("Pętla wykonana {} razy".format(licznik))
#   await ctx.send("NWD to: {}".format(cyfra1))


load_dotenv()
TOKEN = os.getenv("Token")
client.run(TOKEN)