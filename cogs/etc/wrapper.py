import aiohttp
import json
import asyncio

MainURL = 'https://kr.api.riotgames.com'

class Wrapper:

    @classmethod
    def Token(cls):
        with open(r"cogs\etc\Auth.json", "r") as Auth:
            token = json.load(Auth)
            RiotAPIToken = token['RiotAPIToken']
            return f'?api_key={RiotAPIToken}'
    
    @classmethod
    def TFTToken(cls):
        with open(r"cogs\etc\Auth.json", "r") as Auth:
            token = json.load(Auth)
            RiotAPIToken = token['RiotTFTAPIToken']
            return f'?api_key={RiotAPIToken}'

    @classmethod
    async def fetch(cls, session, url):
        async with session.get(url) as response:
            return await response.json()
    
    @classmethod
    async def summoner(cls, summonername):
        async with aiohttp.ClientSession() as session:
            json = await cls.fetch(session, f'{MainURL}/lol/summoner/v4/summoners/by-name/{summonername}{cls.Token()}')
            return json

    @classmethod
    async def league(cls, summonerid):
        async with aiohttp.ClientSession() as session:
            json = await cls.fetch(session, f'{MainURL}/lol/league/v4/entries/by-summoner/{summonerid}{cls.Token()}')
            return json
    
    @classmethod
    async def tftsummoner(cls, summonername):
        async with aiohttp.ClientSession() as session:
            json = await cls.fetch(session, f'{MainURL}/tft/summoner/v1/summoners/by-name/{summonername}{cls.TFTToken()}')
            return json

    @classmethod
    async def tftleague(cls, summonerid):
        async with aiohttp.ClientSession() as session:
            json = await cls.fetch(session, f'{MainURL}/tft/league/v1/entries/by-summoner/{summonerid}{cls.TFTToken()}')
            return json

    @classmethod
    async def status(cls):
        async with aiohttp.ClientSession() as session:
            json = await cls.fetch(session, f'{MainURL}/lol/status/v3/shard-data/{cls.Token()}')
            return json
    
