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

Run the scrape_steam.py file in order to store the steam prices in the redis databases.
```
python3 scrape_steam.py
```

### scrape_steam.py

Takes a game name (must be exact) and gets the price of the game off of the steam library. It stores
the price as a hash in the redis database. 
