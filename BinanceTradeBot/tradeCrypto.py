import schedule
import time

from .BinanceAPIManager import BinanceAPIManager
from .config import Config
from .database import Database
from .logger import Logger
from .strategies import get_strategy

def job():
    print("I'm working from schedule")

def main():
    print('output from main class')
    logger = Logger()
    config = Config()
    database = Database()
    manager = BinanceAPIManager(config)
    schedule.every().second.do(job)

    streategy = get_strategy()

    while True:
        schedule.run_pending()
        time.sleep(1)
