import aiohttp
import json
import asyncio

MainURL = 'https://kr.api.riotgames.com'

class Wrapper:
    def __init__(self, leaguetoken = None, tfttoken = None):
        self.leaguetoken = leaguetoken
        self.tfttoken = tfttoken

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.json()
    
    async def summoner(self, summonername):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/lol/summoner/v4/summoners/by-name/{summonername}{self.leaguetoken}')
            return json

    async def league(self, summonerid):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/lol/league/v4/entries/by-summoner/{summonerid}{self.leaguetoken}')
            return json
    
    async def tftsummoner(self, summonername):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/tft/summoner/v1/summoners/by-name/{summonername}{self.tfttoken}')
            return json

    async def tftleague(self, summonerid):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/tft/league/v1/entries/by-summoner/{summonerid}{self.tfttoken}')
            return json

    async def status(self):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/lol/status/v3/shard-data/{self.leaguetoken}')
            return json
    
