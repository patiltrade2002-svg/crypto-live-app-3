import json
import websockets
from feeds.shared import PRICES

PAIRS = {
    "XBT/USD": "BTC",
    "ETH/USD": "ETH",
    "SOL/USD": "SOL",
    "ADA/USD": "ADA",
    "XRP/USD": "XRP",
    "DOGE/USD": "DOGE",
    "LINK/USD": "LINK",
    "AVAX/USD": "AVAX",
    "MATIC/USD": "MATIC",
    "DOT/USD": "DOT",
}

async def run_kraken():
    uri = "wss://ws.kraken.com"

    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({
            "event": "subscribe",
            "pair": list(PAIRS),
            "subscription": {"name": "ticker"}
        }))

        while True:
            msg = json.loads(await ws.recv())
            if isinstance(msg, list):
                coin = PAIRS.get(msg[-1])
                if coin:
                    PRICES[coin]["Kraken"] = float(msg[1]["c"][0])
