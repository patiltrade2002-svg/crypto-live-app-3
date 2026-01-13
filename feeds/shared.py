from feeds.config import COINS


COINS = [
    "BTC", "ETH", "SOL", "ADA", "XRP",
    "DOGE", "AVAX", "DOT", "LINK", "MATIC",
    "ATOM", "UNI", "LTC", "BCH", "TRX",
    "ICP", "FIL", "NEAR", "APT", "OP"
]

PRICES = {coin: {} for coin in COINS}
