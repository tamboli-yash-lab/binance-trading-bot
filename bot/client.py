from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

class BinanceClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)

    def test_connection(self):
        try:
            account_info = self.client.futures_account()
            return account_info
        except Exception as e:
            raise Exception(f"Connection failed:{str(e)}")