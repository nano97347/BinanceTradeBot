from .BinanceAPIManager import BinanceAPIManager
from .config import Config
import schedule
import time
def main():
    manager = BinanceAPIManager(Config())
    print('output from main class')

def job():
    print("I'm working...")

schedule.every().second.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
