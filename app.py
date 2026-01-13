import asyncio
import streamlit as st
import pandas as pd

from feeds.shared import PRICES, COINS
from feeds.coinbase import coinbase_ws
from feeds.kraken import kraken_ws
from feeds.arbitrage import find_arbitrage

st.set_page_config(page_title="Crypto Arbitrage", layout="wide")
st.title("⚡ Live Crypto Arbitrage Scanner")

# ---- Start background websocket tasks ONCE ----
@st.cache_resource
def start_ws_tasks():
    loop = asyncio.get_event_loop()
    loop.create_task(coinbase_ws())
    loop.create_task(kraken_ws())

start_ws_tasks()

# ---- UI Refresh ----
st.caption("Live prices from Coinbase & Kraken (WebSockets)")

rows = []

for coin in COINS:
    prices = PRICES.get(coin)
    if not prices or len(prices) < 2:
        continue

    result = find_arbitrage(coin, prices)
    if result:
        rows.append(result)

if rows:
    df = pd.DataFrame(rows).sort_values("net_profit", ascending=False)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Waiting for live price data...")

# auto-refresh
st.sleep(2)
st.rerun()
