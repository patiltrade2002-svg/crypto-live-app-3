import asyncio
import json
import websockets
from feeds.shared import PRICES, COINS

KRAKEN_WS = "wss://ws.kraken.com"

PAIR_MAP = {c: f"{c}/USD" for c in COINS}

async def kraken_ws():
    while True:
        try:
            async with websockets.connect(KRAKEN_WS, ping_interval=20) as ws:
                subscribe = {
                    "event": "subscribe",
                    "pair": list(PAIR_MAP.values()),
                    "subscription": {"name": "ticker"}
                }
                await ws.send(json.dumps(subscribe))

                async for msg in ws:
                    data = json.loads(msg)
                    if isinstance(data, list):
                        pair = data[-1]
                        coin = pair.split("/")[0]
                        price = float(data[1]["c"][0])
                        PRICES.setdefault(coin, {})["kraken"] = price

        except Exception as e:
            print("Kraken WS error:", e)
            await asyncio.sleep(5)
