# feeds/config.py

# Trading fees (approximate taker fees)
FEES = {
    "coinbase": 0.006,   # 0.6%
    "kraken": 0.004,     # 0.4%
}
COINS = {
    # Coinbase + Kraken confirmed
    "BTC":  {"coinbase": "BTC-USD",  "kraken": "XBT/USD"},
    "ETH":  {"coinbase": "ETH-USD",  "kraken": "ETH/USD"},
    "SOL":  {"coinbase": "SOL-USD",  "kraken": "SOL/USD"},
    "ADA":  {"coinbase": "ADA-USD",  "kraken": "ADA/USD"},
    "XRP":  {"coinbase": "XRP-USD",  "kraken": "XRP/USD"},
    "DOGE": {"coinbase": "DOGE-USD", "kraken": "DOGE/USD"},
    "LINK": {"coinbase": "LINK-USD", "kraken": "LINK/USD"},
    "AVAX": {"coinbase": "AVAX-USD", "kraken": "AVAX/USD"},
    "MATIC":{"coinbase": "MATIC-USD","kraken": "MATIC/USD"},
    "DOT":  {"coinbase": "DOT-USD",  "kraken": "DOT/USD"},
}
