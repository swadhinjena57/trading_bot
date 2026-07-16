from bot.logging_config import logger


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_order(
            self,
            symbol,
            side,
            order_type,
            quantity,
            price=None
    ):

        try:

            logger.info(
                f"Request: {symbol} {side} {order_type} Qty={quantity} Price={price}"
            )

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "LIMIT":

                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(**params)

            logger.info(response)

            return response

        except Exception as e:

            logger.error(str(e))

            raise