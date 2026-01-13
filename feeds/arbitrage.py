from feeds.shared import PRICES
from feeds.config import FEES

def find_arbitrage():
    opportunities = []

    for coin, exchanges in PRICES.items():
        if len(exchanges) < 2:
            continue

        buy_ex, buy_price = min(exchanges.items(), key=lambda x: x[1])
        sell_ex, sell_price = max(exchanges.items(), key=lambda x: x[1])

        if buy_price <= 0:
            continue

        gross_pct = (sell_price - buy_price) / buy_price * 100
        fee_pct = (FEES.get(buy_ex, 0) + FEES.get(sell_ex, 0)) * 100
        net_pct = gross_pct - fee_pct

        if net_pct > 0:
            opportunities.append({
                "Coin": coin,
                "Buy @": buy_ex,
                "Buy Price": round(buy_price, 4),
                "Sell @": sell_ex,
                "Sell Price": round(sell_price, 4),
                "Net Profit %": round(net_pct, 3)
            })

    return sorted(opportunities, key=lambda x: x["Net Profit %"], reverse=True)
