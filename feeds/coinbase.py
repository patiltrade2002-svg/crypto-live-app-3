import asyncio
import json
import websockets
from feeds.shared import PRICES, COINS

COINBASE_WS = "wss://ws-feed.exchange.coinbase.com"

async def coinbase_ws():
    while True:
        try:
            async with websockets.connect(COINBASE_WS, ping_interval=20) as ws:
                subscribe = {
                    "type": "subscribe",
                    "channels": [{
                        "name": "ticker",
                        "product_ids": [f"{c}-USD" for c in COINS]
                    }]
                }
                await ws.send(json.dumps(subscribe))

                async for msg in ws:
                    data = json.loads(msg)
                    if data.get("type") == "ticker":
                        coin = data["product_id"].split("-")[0]
                        price = float(data["price"])
                        PRICES.setdefault(coin, {})["coinbase"] = price

        except Exception as e:
            print("Coinbase WS error:", e)
            await asyncio.sleep(5)
