import discord
from discord.ext import commands
import json
from cogs.etc.botembed import BotEmbed
from cogs.etc.wrapper import Wrapper

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(name="서버상태")
    async def serverstatus(self, ctx):
        riot = Wrapper(leaguetoken="token paste here")
        rawstatus = await riot.status()

        check_status = []
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

        def checkstatus():
            if 'online' in game_status:
                pass
            else:
                check_status.append("게임")

            if 'online' in store_status:
                pass
            else:
                check_status.append("스토어")

            if 'online' in website_status:
                pass
            else:
                check_status.append("웹사이트")

            if 'online' in client_status:
                pass
            else:
                check_status.append("클라이언트")
            assert(len(check_status) == 0)

        try:
            checkstatus()
        except AssertionError as e:
            embed = discord.Embed(title="서버문제가있는거같아요!", description=f"\n{' '.join(check_status)}서버 문제가있어요")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="모든게 정상적이에요!")
            await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Status(bot))