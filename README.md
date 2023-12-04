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

### games_app.py

Flask server that references steam prices and returns jsonified data to our front-end display