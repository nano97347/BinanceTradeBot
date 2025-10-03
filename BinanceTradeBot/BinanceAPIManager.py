from .config import Config
from binance.client import Client # pip install python-binance

class BinanceAPIManager:
    def __init__(self, config:Config):
        self.binance_client = Client(
            config.BINANCE_API_KEY,
            config.BINANCE_API_SECRET_KEY,
        )
        print('BinanceAPIManager')
