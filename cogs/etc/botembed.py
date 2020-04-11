import discord
from discord.ext import commands
    
class BotEmbed:
    #wait info
    waitinfoembed = discord.Embed(title="서버로부터 요청하는중이에요!", description = "잠시만기다려주세요.....")
    waitinfoembed.set_footer(text="이 메세지가 계속뜨고 지속된다면 명령어를 맞게,없는정보를 요청하였는지확인하고\n 그래도 이문제가 계속될경우 봇에게 DM해주세요.")
