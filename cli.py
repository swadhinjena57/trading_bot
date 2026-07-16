import argparse
import sys

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import *

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True)
parser.add_argument("--price")

args = parser.parse_args()

try:

    symbol = args.symbol.upper()

    side = validate_side(args.side)

    order_type = validate_order_type(args.type)

    quantity = validate_quantity(args.quantity)

    price = validate_price(args.price)

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order requires price")

    client = BinanceClient().client

    manager = OrderManager(client)

    response = manager.place_order(
        symbol,
        side,
        order_type,
        quantity,
        price
    )

    print("\n========= ORDER SUMMARY =========")

    print("Symbol :", symbol)
    print("Side :", side)
    print("Type :", order_type)
    print("Quantity :", quantity)

    if price:
        print("Price :", price)

    print("\n========= RESPONSE =========")

    print("Order ID :", response.get("orderId"))

    print("Status :", response.get("status"))

    print("Executed Qty :", response.get("executedQty"))

    print("Average Price :", response.get("avgPrice"))

    print("\nOrder Placed Successfully")

except Exception as e:

    print("\nOrder placement failed")
    print(f"Error: {e}")

    if "-2015" in str(e):
        print("Hint: Use Binance Futures Testnet API keys in .env, enable Futures permission, and verify IP restrictions.")

    sys.exit(1)