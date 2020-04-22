import aiohttp
import json
import asyncio

MainURL = 'https://kr.api.riotgames.com'

class Wrapper:
    def Token(self):
        with open(r"cogs\etc\Auth.json", "r") as Auth:
            token = json.load(Auth)
            RiotAPIToken = token['RiotAPIToken']
            return RiotAPIToken
        
    def TFTToken(self):
        with open(r"cogs\etc\Auth.json", "r") as Auth:
            token = json.load(Auth)
            RiotAPIToken = token['RiotTFTAPIToken']
            return RiotAPIToken

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.json()
    
    async def summoner(self, summonername):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/lol/summoner/v4/summoners/by-name/{summonername}?api_key={self.Token()}')
            return json

    async def league(self, summonerid):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/lol/league/v4/entries/by-summoner/{summonerid}?api_key={self.Token()}')
            return json
    
    async def tftsummoner(self, summonername):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/tft/summoner/v1/summoners/by-name/{summonername}?api_key={self.TFTToken()}')
            return json

    async def tftleague(self, summonerid):
        async with aiohttp.ClientSession() as session:
            json = await self.fetch(session, f'{MainURL}/tft/league/v1/entries/by-summoner/{summonerid}?api_key={self.TFTToken()}')
            return json
    
