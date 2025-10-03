import time

from .BinanceAPIManager import BinanceAPIManager
from .config import Config

def main():
    config = Config()
    manager = BinanceAPIManager(config)
    print('output from main class')
