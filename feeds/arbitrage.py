from feeds.config import FEES

def find_arbitrage(coin, prices):
    buy_ex = min(prices, key=prices.get)
    sell_ex = max(prices, key=prices.get)

    buy_price = prices[buy_ex]
    sell_price = prices[sell_ex]

    gross = sell_price - buy_price
    net = gross - (buy_price * FEES[buy_ex]) - (sell_price * FEES[sell_ex])

    if net <= 0:
        return None

    return {
        "coin": coin,
        "buy_from": buy_ex,
        "sell_to": sell_ex,
        "buy_price": round(buy_price, 2),
        "sell_price": round(sell_price, 2),
        "net_profit": round(net, 2),
    }
