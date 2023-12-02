# Flask server to display data from redis database

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import redis
import requests
import secrets
import os

app = Flask(__name__)
# Create a secret key for the session (to sign off on the cookies)
app.secret_key = os.environ.get('SECRET_KEY') or secrets.token_hex(16)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Basic registration and login system
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user details from form
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if r.exists(f"user:{username}:password"):
            return 'Username already exists'

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Save user in Redis
        r.set(f"user:{username}:password", hashed_password)

        # Redirect to login page after registration
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve user password from Redis and validate
        stored_password = r.get(f"user:{username}:password")
        if stored_password and check_password_hash(stored_password, password):
            session['username'] = username
            return redirect(url_for('index'))  # Redirect to main page after login
        else:
            return 'Login Failed'

    return render_template('login.html')


@app.route('/games/<name>', methods=['GET', 'POST'])
def get_game(name):
    target_id = find_target_game_id(name)
    gamePrice = get_game_price(target_id)
    return jsonify({'name': name,
                    'price': gamePrice})
    

@app.route('/gamedata/<name>', methods=['GET', 'POST'])
def display_game_data_from_steam(name):
    target_id = find_target_game_id(name)
    url = 'http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=' + str(target_id) + '&count=3&maxlength=500&format=json'
    response = requests.get(url)
    news_list = []
    for news in response.json()['appnews']['newsitems']:
        news_list.append(news['contents'])
    return news_list


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


def find_target_game_id(game_name):
    if game_name in game_names:
        target_id = ""
        for id in app_ids:
            if id["name"] == game_name:
                target_id = id["appid"]
                break
        return target_id
    else:
        return "Game not found"


if __name__ == "__main__":
    app_ids = get_app_ids_for_steam_games()
    game_names = []
    for id in app_ids:
        game_names.append(id["name"])
    app.run(debug=True, port=8000)
