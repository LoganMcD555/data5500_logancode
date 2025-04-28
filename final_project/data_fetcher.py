import requests
import os
from datetime import datetime

# CoinGecko IDs
coin_ids = {
    'btc': 'bitcoin',
    'eth': 'ethereum',
    'ltc': 'litecoin',
    'xrp': 'ripple',
    'bch': 'bitcoin-cash',
    'doge': 'dogecoin',
    'ada': 'cardano',
    'sol': 'solana',
    'avax': 'avalanche-2',
    'matic': 'matic-network',
    'dot': 'polkadot',
    'shib': 'shiba-inu'
}

# Currency pairs to evaluate
pairs = [
    ('btc', 'eth'), ('btc', 'ada'), ('btc', 'sol'), ('btc', 'dot'), ('btc', 'doge'),
    ('eth', 'btc'), ('eth', 'matic'), ('eth', 'ltc'), ('eth', 'shib'), ('eth', 'avax'),
    ('ada', 'btc'), ('ada', 'eth'), ('ada', 'xrp'), ('ada', 'dot'),
    ('sol', 'btc'), ('sol', 'eth'), ('sol', 'ada'), ('sol', 'matic'),
    ('dot', 'btc'), ('dot', 'eth'), ('dot', 'shib'), ('dot', 'avax'),
    ('doge', 'btc'), ('doge', 'eth'), ('doge', 'shib'), ('doge', 'ltc'),
    ('ltc', 'btc'), ('ltc', 'eth'), ('ltc', 'doge'),
    ('bch', 'btc'), ('bch', 'eth'), ('bch', 'ltc'),
    ('xrp', 'btc'), ('xrp', 'eth'), ('xrp', 'ada'),
    ('matic', 'btc'), ('matic', 'eth'), ('matic', 'sol'),
    ('avax', 'btc'), ('avax', 'eth'), ('avax', 'dot')
]

# Build the request
all_ids = ','.join(set(coin_ids.values()))
url = "https://api.coingecko.com/api/v3/simple/price?ids=" + all_ids + "&vs_currencies=usd"
response = requests.get(url)
usd_data = response.json()

# Parse USD prices
usd_prices = {}
for symbol, gecko_id in coin_ids.items():
    try:
        usd_prices[symbol] = usd_data[gecko_id]['usd']
    except KeyError:
        print("Missing price for", symbol)

# Prepare file saving
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, 'data')
os.makedirs(data_dir, exist_ok=True)

# Use date + time so each run is unique
timestamp = datetime.now().strftime("%Y.%m.%d_%H.%M")

# Loop through each pair and save rate
for from_coin, to_coin in pairs:
    if from_coin in usd_prices and to_coin in usd_prices:
        rate = usd_prices[from_coin] / usd_prices[to_coin]
        filename = os.path.join(data_dir, from_coin.upper() + "_" + to_coin.upper() + "_" + timestamp + ".txt")
        with open(filename, 'w') as f:
            f.write("currency_from,currency_to,exchange_rate\n")
            f.write(from_coin.upper() + "," + to_coin.upper() + "," + str(round(rate, 8)) + "\n")
        print("Saved:", filename)
    else:
        print("Skipped", from_coin, "to", to_coin, "due to missing price")
