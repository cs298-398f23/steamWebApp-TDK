#Steam Domain Name: 398WebProgramming

import requests
import redis

def get_game_id(game_name):
    params = {"term": game_name, "l": "english", "cc": "us"}
    request = requests.get("http://store.steampowered.com/api/storesearch/", params=params)
    json = request.json()
    return json["items"][0]["id"]

def get_game_price(game_id):
    params = {"appids": game_id, "cc": "us", "filters": "price_overview"}
    request = requests.get("http://store.steampowered.com/api/appdetails?appids=", params=params)
    json = request.json()
    return json[str(game_id)]["data"]["price_overview"]["final_formatted"]

if __name__ == "__main__":
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    game_name = "terraria"
    game_id = get_game_id(game_name)
    game_price = get_game_price(game_id)
    r.hset(game_name, mapping={
        "steam_price": game_price}
        )