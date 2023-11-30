#Steam Domain Name: 398WebProgramming

import requests
import redis

def get_steam_games():
    params = {"l": "english", "cc": "us"}
    request = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/", params=params)
    json = request.json()
    return json["applist"]["apps"]

# def get_game_price(game_id):
#     params = {"appids": game_id, "cc": "us", "filters": "price_overview"}
#     request = requests.get("http://store.steampowered.com/api/appdetails?appids=", params=params)
#     json = request.json()
#     return json[str(game_id)]["data"]["price_overview"]["final_formatted"]

if __name__ == "__main__":
    games = get_steam_games()
    games_list = [game["name"] for game in games if game["name"] != ""]
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.set("games", str(games_list))
    