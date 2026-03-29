from flask import Flask, jsonify
import random

app = Flask(__name__)

SYMBOLS = ["EURUSD", "GBPUSD", "XAUUSD"]

def generate_signal(symbol):
    action = random.choice(["BUY", "SELL"])
    entry = round(random.uniform(1.0, 2.0), 5)

    if action == "BUY":
        sl = round(entry - 0.0020, 5)
        tp = round(entry + 0.0040, 5)
    else:
        sl = round(entry + 0.0020, 5)
        tp = round(entry - 0.0040, 5)

    return {
        "pair": symbol,
        "action": action,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "confidence": random.randint(70, 90)
    }
@app.route('/')
def home():
    return "Forex Signal Bot is running 🚀".
@app.route('/signals')
def signals():
    return jsonify([generate_signal(s) for s in SYMBOLS])

if __name__ == "__main__":
    app.run()
from flask import Flask, jsonify
import random

app = Flask(__name__)

SYMBOLS = ["EURUSD", "GBPUSD", "XAUUSD"]

@app.route('/')
def home():
    return "Forex Signal Bot is running 🚀"

def generate_signal(symbol):
    action = random.choice(["BUY", "SELL"])
    entry = round(random.uniform(1.0, 2.0), 5)

    if action == "BUY":
        sl = round(entry - 0.0020, 5)
        tp = round(entry + 0.0040, 5)
    else:
        sl = round(entry + 0.0020, 5)
        tp = round(entry - 0.0040, 5)

    return {
        "pair": symbol,
        "action": action,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "confidence": random.randint(70, 90)
    }

@app.route('/signals')
def signals():
    return jsonify([generate_signal(s) for s in SYMBOLS])

if __name__ == "__main__":
    app.run()
