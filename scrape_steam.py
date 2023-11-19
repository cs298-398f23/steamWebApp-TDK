#Steam Domain Name: 398WebProgramming

import requests
import redis

def get_steam_games():
    params = {"l": "english", "cc": "us"}
    request = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/", params=params)
    json = request.json()
    return json["applist"]["apps"]

def get_game_price(game_id):
    params = {"appids": game_id, "cc": "us", "filters": "price_overview"}
    request = requests.get("http://store.steampowered.com/api/appdetails?appids=", params=params)
    json = request.json()
    return json[str(game_id)]["data"]["price_overview"]["final_formatted"]

def add_game_to_redis(game_name, game_price, r):
    r.hset(game_name, mapping={
        "steam_price": game_price}
        )

if __name__ == "__main__":
    count = 1
    games = get_steam_games()
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    for game in games:
        if game["name"] != "":
            try: 
                game_price = get_game_price(game["appid"])
                add_game_to_redis(game["name"].lower(), game_price, r)
            except Exception as e:
                pass
            print(count)
            count += 1
    