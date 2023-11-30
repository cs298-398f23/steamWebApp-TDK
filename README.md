# steamWebApp-TDK

### Getting Started

Start a python virtual environment and install the requirements using requirements.txt.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the redis database to store the information.

```
redis-server
```

Run the add_games_to_redis.py file in order to store the steam game names in the redis databases.
```
python3 add_games_to_redis.py
```

### add_games_to_redis.py

Hits the Steam API and stores a reference string of game names to be used as verification for price calling

### games_app.py

Flask server that references steam prices and returns jsonified data to our front-end display