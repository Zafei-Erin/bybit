from api import apiKey, apiSecret
from pybit.unified_trading import HTTP

session = HTTP(
    testnet=True,
    api_key=apiKey,
    api_secret=apiSecret,
)


def get_balance(coin):
    try:
        resp = session.get_wallet_balance(accountType="UNIFIED", coin=coin)
        walletBalance = resp["result"]["list"][0]["coin"][0]["walletBalance"]
        walletBalance = float(0 if walletBalance == '' else walletBalance)
        return walletBalance
    except Exception as err:
        print(err)


def place_order():
    try:
        resp = session.place_order(
            category="spot",
            symbol="ETHUSDT",
            side="Buy",
            orderType="Limit",
            qty="0.1",
            price="100",
            timeInForce="PostOnly",
            isLeverage=0,
            orderFilter="Order")
        orderId = resp["result"]["orderId"]
        print("place order successfully, orderId:", orderId)
    except Exception as err:
        print(err)


place_order()
