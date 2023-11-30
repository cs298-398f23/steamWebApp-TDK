# Flask server to display data from redis database

from flask import Flask, render_template, request, jsonify
import redis
import requests


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/games/<name>', methods=['GET', 'POST'])
def get_game(name):
    if name in game_list:
        target_id = ""
        for id in app_ids:
            if id["name"] == name:
                target_id = id["appid"]
                break
        gamePrice = get_game_price(target_id)
        return jsonify({'name': name,
                        'price': gamePrice})
    else:
        return jsonify({'error': 'Game not found'})


def get_redis():
    return redis.Redis(host='localhost', port=6379, decode_responses=True)


def parse_games(games):
    game_list = []
    games = games.split(",")
    for game in games:
        game_list.append(game.strip().strip("'").strip('"'))
    return game_list


def get_game_price(game_id):
    params = {"appids": game_id, "cc": "us", "filters": "price_overview"}
    request = requests.get("http://store.steampowered.com/api/appdetails?appids=", params=params)
    json = request.json()
    return json[str(game_id)]["data"]["price_overview"]["final_formatted"]


def get_app_ids_for_steam_games():
    params = {"l": "english", "cc": "us"}
    request = requests.get("http://api.steampowered.com/ISteamApps/GetAppList/v0002/", params=params)
    json = request.json()
    return json["applist"]["apps"]


if __name__ == "__main__":
    r = get_redis()
    game_names = r.get("games")
    game_list = parse_games(game_names)
    app_ids = get_app_ids_for_steam_games()
    app.run(debug=True, port=8000)