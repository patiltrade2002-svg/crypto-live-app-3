import json
import websockets
from feeds.shared import PRICES

PRODUCTS = {
    "BTC-USD": "BTC",
    "ETH-USD": "ETH",
    "SOL-USD": "SOL",
    "ADA-USD": "ADA",
    "XRP-USD": "XRP",
    "DOGE-USD": "DOGE",
    "LINK-USD": "LINK",
    "AVAX-USD": "AVAX",
    "MATIC-USD": "MATIC",
    "DOT-USD": "DOT",
}

async def run_coinbase():
    uri = "wss://ws-feed.exchange.coinbase.com"

    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({
            "type": "subscribe",
            "channels": [{"name": "ticker", "product_ids": list(PRODUCTS)}]
        }))

        while True:
            msg = json.loads(await ws.recv())
            if msg.get("type") == "ticker":
                coin = PRODUCTS.get(msg["product_id"])
                if coin:
                    PRICES[coin]["Coinbase"] = float(msg["price"])
