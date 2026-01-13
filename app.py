import time
import streamlit as st
import pandas as pd

from feeds.shared import COINS
from feeds.coinbase import get_coinbase_prices
from feeds.kraken import get_kraken_prices
from feeds.arbitrage import find_arbitrage

st.set_page_config(page_title="Crypto Arbitrage Scanner", layout="wide")
st.title("⚡ Live Crypto Arbitrage Scanner (REST)")

st.caption("Coinbase + Kraken | REST polling (stable & fast)")

# ---- Fetch prices ----
coinbase_prices = get_coinbase_prices()
kraken_prices = get_kraken_prices()

# ---- SHOW RAW PRICES (IMPORTANT) ----
price_rows = []

for coin in COINS:
    price_rows.append({
        "coin": coin,
        "coinbase": coinbase_prices.get(coin),
        "kraken": kraken_prices.get(coin),
    })

price_df = pd.DataFrame(price_rows)
st.subheader("📊 Live Prices")
st.dataframe(price_df, use_container_width=True)

# ---- Arbitrage ----
arb_rows = []

for coin in COINS:
    prices = {}
    if coin in coinbase_prices:
        prices["coinbase"] = coinbase_prices[coin]
    if coin in kraken_prices:
        prices["kraken"] = kraken_prices[coin]

    if len(prices) < 2:
        continue

    result = find_arbitrage(coin, prices)
    if result:
        arb_rows.append(result)

st.subheader("💰 Arbitrage Opportunities")

if arb_rows:
    arb_df = pd.DataFrame(arb_rows).sort_values("net_profit", ascending=False)
    st.dataframe(arb_df, use_container_width=True)
else:
    st.info("No profitable arbitrage after fees")

# ---- Refresh ----
time.sleep(2)
st.rerun()
