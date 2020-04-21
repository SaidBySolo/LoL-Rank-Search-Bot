import discord
from discord.ext import commands
from riotwatcher import LolWatcher
import json
from cogs.etc.botembed import BotEmbed
from cogs.etc.riot import watcher

region = "kr"
watcher = watcher()

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(name="서버상태")
    async def serverstatus(self, ctx):
        rawstatus = watcher.lol_status.shard_data(region)
        name = rawstatus['name']
        services = rawstatus['services']

        game = services[0]
        store = services[1]
        website = services[2]
        client = services[3]

        game_status = game['status']
        store_status = store['status']
        website_status = website['status']
        client_status = client['status']

        embed = discord.Embed(title=f"{name}의 서버 상태입니다")

def setup(bot):
    bot.add_cog(Status(bot))