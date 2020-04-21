import aiohttp
import json
import asyncio

class Rapper:
    def Token(self):
        with open(r"cogs\etc\Auth.json", "r") as Auth:
            token = json.load(Auth)
            RiotAPIToken = token['RiotAPIToken']
            return RiotAPIToken

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.json()

    async def summoner(self, summonername):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonername}?api_key={self.Token()}')
            return json

    async def league(self, summonerid):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerid}?api_key={self.Token()}')
            return json


