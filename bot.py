import discord
from discord.ext import commands
import json

with open(r"cogs\etc\Auth.json", "r") as Auth:
    loadjson = json.load(Auth)

token = loadjson['DiscordToken']

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="&")

def load_cogs(bot):
    extensions = ['cogs.status',
                'cogs.solo5x5',
                'cogs.flexsr',
                'cogs.events']


    failed = []

    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"{e.__class__.__name__}: {str(e)}")
            failed.append(extension)

    if failed:
        print(f"\n{' '.join(failed)}를 로드하는데 실패했습니다.\n")
    return failed
    

if __name__ == '__main__':
    bot = Bot()
    load_cogs(bot)
    bot.run(token)