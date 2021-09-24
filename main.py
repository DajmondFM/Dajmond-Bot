from nextcord.ext import commands
import os




bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')

my_secret = os.environ['Token']
bot.run('my_secret')