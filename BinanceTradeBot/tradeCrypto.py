from .BinanceAPIManager import BinanceAPIManager
from .config import Config
import schedule
import time

# https://docs.python.org/3/library/logging.html
from .logger import Logger

def job():
    print("I'm working from schedule")

def main():
    logger = Logger()

    config = Config()
    manager = BinanceAPIManager(config)
    print('output from main class')
    schedule.every().second.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
