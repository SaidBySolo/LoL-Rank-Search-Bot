import discord
from discord.ext import commands
import json

with open("cogs\etc\Auth.json", "r") as Auth:
    loadjson = json.load(Auth)

token = loadjson['DiscordToken']

bot = commands.Bot(command_prefix="$")

extensions = ['cogs.solo5x5',
            'cogs.flexsr',
            'cogs.events']

for extention in extensions:
    bot.load_extension(extention)

bot.run(token)