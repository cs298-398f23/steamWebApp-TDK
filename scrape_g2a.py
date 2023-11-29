import requests
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Get the API_KEY from the environment variables
G2A_API_KEY = os.getenv("G2A_API_KEY")

def get_g2a_game_id(game_name):
    headers = {'Authorization': f'Bearer {G2A_API_KEY}'}
    params = {"search": game_name}
    response = requests.get("https://api.g2a.com/v1/catalog/products", headers=headers, params=params)
    json_data = response.json()
    # Assume the first result is the correct game
    return json_data["products"][0]["id"]

def get_game_price(game_id):
    headers = {'Authorization': f'Bearer {G2A_API_KEY}'}
    response = requests.get(f"https://api.g2a.com/v1/catalog/products/{game_id}", headers=headers)
    json_data = response.json()
    return json_data["price"]

def add_game_to_redis(game_name, game_price, r):
    r.hset(game_name, mapping={
        "g2a_price": game_price}
        )

if __name__ == "__main__":
    # r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    # Example usage
    game_name = "Cyberpunk 2077"  # Replace with the game you want to check
    game_id = get_g2a_game_id(game_name)
    game_price = get_game_price(game_id)
    # add_game_to_redis(game_name.lower(), game_price, r)