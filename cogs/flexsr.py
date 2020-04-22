import discord
from discord.ext import commands
import json
from cogs.etc.riotdict import RiotDict
from cogs.etc.botembed import BotEmbed
from cogs.etc.wrapper import Wrapper

class Solo5x5(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="자랭")
    async def freerank(self, ctx, *, user):
        wrapper = Wrapper()
        waitinfo = await ctx.send(embed = BotEmbed.waitinfoembed)
        try:
            summonerinfo = await Wrapper.summoner(summonername = user)
        except Exception:
            nouserembed = discord.Embed(title=f"존재하지않는 유저인거같아요",description="확인후 다시시도 해주세요")
            await waitinfo.edit(embed=nouserembed)

        summonername = summonerinfo['name']
        summonerid = summonerinfo['id']
        summonerenid = summonerinfo['accountId']
        summonerlv = summonerinfo['summonerLevel']

        summonerranks = await Wrapper.league(summonerid = summonerid)

        if not summonerranks:
            nrembed = discord.Embed(title=f"{summonername}님의 랭크 정보가 없는거 같아요...",description="확인후 다시시도 해주세요")
            await waitinfo.edit(embed=nrembed)
        elif len(summonerranks) == 2:
            summonerranks = summonerranks[1]
        else:
            summonerranks = summonerranks[0]

        queuetype = RiotDict.riotdict[summonerranks['queueType']]
        tear = RiotDict.riotdict[summonerranks['tier']]
        rank = RiotDict.riotdict[summonerranks['rank']]
        point = summonerranks['leaguePoints']
        win = summonerranks['wins']
        loss = summonerranks['losses']
        
        if queuetype == "솔로랭크":
            nsrembed = discord.Embed(title=f"{summonername}님의 자유랭크 정보가 없는거 같아요...",description="확인후 다시시도 해주세요")
            await waitinfo.edit(embed=nsrembed)
        else:
            #embed
            embed = discord.Embed(title=f"{summonername}님의 검색 결과입니다.", description=f"{queuetype}")
            embed.set_thumbnail(url=RiotDict.riotdict[f'{tear}img'])
            embed.add_field(name="레벨", value=f"{summonerlv}레벨", inline=True)
            embed.add_field(name=f"{tear} {rank}", value=f"{point}LP", inline=True)
            embed.add_field(name="승/패", value=f"{win}승/{loss}패", inline=True)
            embed.add_field(name="승률", value=f"{round(win/(win+loss)*100, 2)}%",inline=True)
            await waitinfo.edit(embed=embed)
            
def setup(bot):
    bot.add_cog(Solo5x5(bot))