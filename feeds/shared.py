from feeds.config import COINS

# Shared price store
# Example:
# PRICES["BTC"] = {"Coinbase": 43000, "Kraken": 43120}

PRICES = {coin: {} for coin in COINS}
