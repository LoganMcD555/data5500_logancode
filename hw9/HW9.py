import requests
import networkx as nx
import math
from itertools import combinations

# Constants
COIN_IDS = [
    'bitcoin', 'ethereum', 'litecoin', 'ripple', 'cardano', 'bitcoin-cash', 'eos'
]
TICKERS = ['btc', 'eth', 'ltc', 'xrp', 'ada', 'bch', 'eos']
ID_TO_TICKER = dict(zip(COIN_IDS, TICKERS))

# Fetch exchange rates from CoinGecko API
url = (
    'https://api.coingecko.com/api/v3/simple/price?ids=' + ','.join(COIN_IDS) +
    '&vs_currencies=' + ','.join(TICKERS)
)
response = requests.get(url)
data = response.json()

# Build directed graph with exchange rates
g = nx.DiGraph()
for base_id in data:
    base_ticker = ID_TO_TICKER[base_id]
    for quote_ticker in data[base_id]:
        if base_ticker != quote_ticker:
            rate = data[base_id][quote_ticker]
            g.add_edge(base_ticker, quote_ticker, weight=rate)

print("\n=== Graph Info ===")
print("Nodes:", list(g.nodes))
print("Edges:", list(g.edges))

min_factor = float('inf')
max_factor = 0
min_paths = ()
max_paths = ()

# Limit path length to avoid explosion
MAX_PATH_LEN = 5

# Evaluate arbitrage opportunities
for source, target in combinations(TICKERS, 2):
    if source not in g or target not in g:
        continue

    forward_paths = list(nx.all_simple_paths(g, source=source, target=target, cutoff=MAX_PATH_LEN))
    reverse_paths = list(nx.all_simple_paths(g, source=target, target=source, cutoff=MAX_PATH_LEN))

    for f_path in forward_paths:
        f_weight = 1.0
        for i in range(len(f_path) - 1):
            f_weight *= g[f_path[i]][f_path[i + 1]]['weight']

        for r_path in reverse_paths:
            r_weight = 1.0
            for i in range(len(r_path) - 1):
                r_weight *= g[r_path[i]][r_path[i + 1]]['weight']

            factor = f_weight * r_weight

            if not math.isclose(factor, 1.0, rel_tol=1e-8):
                print("\n--- Arbitrage Opportunity ---")
                print("From", source, "to", target)
                print("FORWARD:", f_path, f_weight)
                print("REVERSE:", r_path, r_weight)
                print("FACTOR:", factor)

            if factor < min_factor:
                min_factor = factor
                min_paths = (f_path, r_path)
            if factor > max_factor:
                max_factor = factor
                max_paths = (f_path, r_path)

# Final summary
print("\n=== Final Results ===")
if min_paths:
    print("Smallest Paths weight factor:", min_factor)
    print("Paths:", min_paths)
else:
    print("No valid paths found for minimum factor.")

if max_paths:
    print("Greatest Paths weight factor:", max_factor)
    print("Paths:", max_paths)
else:
    print("No valid paths found for maximum factor.")
