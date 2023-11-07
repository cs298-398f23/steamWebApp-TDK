# Get user games
# http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=XXXXXXXXXXXXXXXXX&steamid=76561197960434622&format=json

# Get Recently Played Games
# http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=XXXXXXXXXXXXXXXXX&steamid=76561197960434622&format=json

import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config['STEAM_API_KEY']
steam_id = config['STEAM_ID']

get_owned_games_url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + api_key + '&steamid=' + steam_id + '&format=json'
get_recently_played_url = 'http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=' + api_key + '&steamid=' + steam_id + '&format=json'

# owned_games = requests.get(get_owned_games_url)

recent_played_games = requests.get(get_recently_played_url)

for game in recent_played_games.json()['response']['games']:
    print('\nGame: ' + game['name'] + '\nHours in Last 2 Weeks: ' + str(game['playtime_2weeks'] / 60))