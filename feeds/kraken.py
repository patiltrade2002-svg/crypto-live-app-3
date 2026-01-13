import requests

KRAKEN_URL = "https://api.kraken.com/0/public/Ticker"

def get_kraken_prices():
    prices = {}
    try:
        pairs = {
            "BTC": "XBTUSD", "ETH": "ETHUSD", "SOL": "SOLUSD", "ADA": "ADAUSD",
            "XRP": "XRPUSD", "DOGE": "DOGEUSD", "AVAX": "AVAXUSD", "DOT": "DOTUSD",
            "LINK": "LINKUSD", "MATIC": "MATICUSD", "ATOM": "ATOMUSD", "UNI": "UNIUSD",
            "LTC": "LTCUSD", "BCH": "BCHUSD", "TRX": "TRXUSD", "ICP": "ICPUSD",
            "FIL": "FILUSD", "NEAR": "NEARUSD", "APT": "APTUSD", "OP": "OPUSD"
        }

        query = ",".join(pairs.values())
        r = requests.get(f"{KRAKEN_URL}?pair={query}", timeout=10).json()

        for coin, pair in pairs.items():
            if pair in r["result"]:
                prices[coin] = float(r["result"][pair]["c"][0])

    except Exception as e:
        print("Kraken error:", e)

    return prices
