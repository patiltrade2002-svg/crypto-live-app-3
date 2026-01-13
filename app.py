import streamlit as st
import threading
import asyncio
import time

from feeds.shared import PRICES
from feeds.coinbase import run_coinbase
from feeds.kraken import run_kraken
from feeds.arbitrage import find_arbitrage

# --------------------------------------------------
# Start WebSocket feeds ONLY ONCE
# --------------------------------------------------
if "feeds_started" not in st.session_state:
    st.session_state.feeds_started = True

    def start_feed(coro):
        asyncio.run(coro())

    threading.Thread(
        target=start_feed,
        args=(run_coinbase,),
        daemon=True
    ).start()

    threading.Thread(
        target=start_feed,
        args=(run_kraken,),
        daemon=True
    ).start()

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(
    page_title="Live Crypto Arbitrage Scanner",
    layout="wide"
)

st.title("⚡ Live Multi-Exchange Arbitrage Scanner")
st.caption("Coinbase + Kraken • Auto-refresh every second")

# --------------------------------------------------
# Live Prices
# --------------------------------------------------
st.subheader("📊 Live Prices")

price_rows = []
for coin, exchanges in PRICES.items():
    row = {"Coin": coin}
    row.update(exchanges)
    price_rows.append(row)

if price_rows and any(len(v) > 0 for v in PRICES.values()):
    st.table(price_rows)
else:
    st.info("Waiting for live price feeds…")

# --------------------------------------------------
# Arbitrage Opportunities
# --------------------------------------------------
st.subheader("💰 Arbitrage Opportunities")

arbs = find_arbitrage()
if arbs:
    st.table(arbs)
else:
    st.info("No profitable arbitrage detected yet")

# --------------------------------------------------
# Auto refresh (Streamlit-safe)
# --------------------------------------------------
time.sleep(1)
st.rerun()
