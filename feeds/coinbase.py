import requests

COINBASE_URL = "https://api.exchange.coinbase.com/products"

def get_coinbase_prices():
    prices = {}
    try:
        products = requests.get(COINBASE_URL, timeout=10).json()
        usd_pairs = [p["id"] for p in products if p["quote_currency"] == "USD"]

        for pair in usd_pairs:
            r = requests.get(f"{COINBASE_URL}/{pair}/ticker", timeout=5).json()
            coin = pair.split("-")[0]
            prices[coin] = float(r["price"])

    except Exception as e:
        print("Coinbase error:", e)

    return prices
