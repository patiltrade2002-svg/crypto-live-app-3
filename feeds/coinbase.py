import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

COINBASE_TICKER = "https://api.exchange.coinbase.com/products/{}/ticker"

COINS = [
    "BTC", "ETH", "SOL", "ADA", "XRP",
    "DOGE", "AVAX", "DOT", "LINK", "MATIC",
    "ATOM", "UNI", "LTC", "BCH", "TRX",
    "ICP", "FIL", "NEAR", "APT", "OP"
]

def get_coinbase_prices():
    prices = {}

    for coin in COINS:
        pair = f"{coin}-USD"
        try:
            r = requests.get(
                COINBASE_TICKER.format(pair),
                headers=HEADERS,
                timeout=5
            )

            if r.status_code != 200:
                continue

            data = r.json()
            prices[coin] = float(data["price"])

        except Exception as e:
            print("Coinbase error:", coin, e)

    return prices
