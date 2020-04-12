from riotwatcher import LolWatcher
import json

def watcher():
    with open("cogs\etc\Auth.json", "r") as Auth:
        token = json.load(Auth)
        watcher = LolWatcher(token['RiotAPIToken'])
        return watcher