# Flask server to display data from redis database

from flask import Flask, render_template, request, jsonify
import redis


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/games/<name>')
def root(name):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    gamePrice = r.hget(name, "steam_price")
    return jsonify({'name': name,
                    'price': gamePrice})


if __name__ == "__main__":
    app.run(debug=True)