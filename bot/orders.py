from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()
class OrderService:
    def __init__(self):
        self.client = BinanceClient().client

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Order response: {order}")
            return order

        except Exception as e:
            logger.error(f"Market order failed: {str(e)}")
            raise Exception(f"Order failed: {str(e)}")

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"Order response: {order}")
            return order

        except Exception as e:
            logger.error(f"Limit order failed: {str(e)}")
            raise Exception(f"Limit order failed: {str(e)}")
