import json
import os
import alpaca_trade_api as tradeapi
from datetime import datetime

# Alpaca paper trading credentials
API_KEY = "PKLUYL7I6D19PYDC450I"
SECRET_KEY = "vudgEcfK2dwlVTudmLgDJ6upB8IhWeXRkOq9QJRg"
BASE_URL = "https://paper-api.alpaca.markets"

# These are the assets allowed to trade on Alpaca
SUPPORTED_SYMBOLS = ["BTC", "ETH", "LTC", "DOGE", "SOL"]

# Load the latest results from the arbitrage scan
def load_results():
    results_path = os.path.join(os.path.dirname(__file__), "results.json")
    try:
        with open(results_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print("Failed to load results.json:", e)
        return []

def submit_trade(api, symbol, cash_balance, profit_percent, traded_symbols):
    if symbol not in SUPPORTED_SYMBOLS or symbol in traded_symbols:
        return cash_balance

    # Decides how much cash to use based on expected profit
    if profit_percent < 0.2:
        fraction = 0.005  # 0.5% of cash
    elif profit_percent < 0.7:
        fraction = 0.01   # 1% of cash
    else:
        fraction = 0.02   # 2% of cash

    notional = cash_balance * fraction
    notional = round(notional, 2)  # 🛠 fix: round to 2 decimals!

    if notional < 5:
        print("Not enough cash to trade", symbol)
        return cash_balance

    try:
        api.submit_order(
            symbol=symbol + "USD",
            notional=notional,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
        print("Trade submitted for", symbol, "with", notional, "USD based on expected profit", profit_percent, "%")
        cash_balance -= notional
        traded_symbols.add(symbol)
    except Exception as e:
        print("Failed to trade", symbol, ":", e)

    return cash_balance
# Main trading runner
if __name__ == "__main__":
    results = load_results()

    if not results:
        print("No results found.")
    else:
        api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")
        account = api.get_account()
        cash_balance = float(account.cash)

        # Sort cycles by profitability
        top_cycle = sorted(results, key=lambda r: -r["profit_percent"])[0]
        print("Top arbitrage cycle:", top_cycle["cycle"])
        print("Estimated profit:", top_cycle["profit_percent"], "%")

        traded_symbols = set()
        success = False
        for symbol in top_cycle["cycle"]:
            if symbol in SUPPORTED_SYMBOLS and symbol not in traded_symbols:
                cash_balance = submit_trade(api, symbol, cash_balance, top_cycle["profit_percent"], traded_symbols)
                success = True
        
        if not success:
            print("No valid trades submitted this cycle.")
        else:
            print("Trade(s) successfully submitted.")
