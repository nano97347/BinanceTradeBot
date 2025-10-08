import configparser
import os

CFG_FL_NAME = "user.cfg"

class Config:
    def __init__(self):
        print('output from Config class')
        config = configparser.ConfigParser()
        config["DEFAULT"] = {
            "bridge": "USDT",
            "use_margin": "no",
            "scout_multiplier": "5",
            "scout_margin": "0.8",
            "scout_sleep_time": "5",
            "hourToKeepScoutHistory": "1",
            "tld": "com",
            "strategy": "default",
            "sell_timeout": "0",
            "buy_timeout": "0",
            "testnet": False,
        }

    if not os.path.exists(CFG_FL_NAME):
        print("No configuration file (user.cfg) found!")
    else:
        config.read(CFG_FL_NAME)

    supported_coin_list = [
        coin.strip() for coin in os.environ.get("SUPPORTED_COIN_LIST", "").split() if coin.strip()
    ]

    if not supported_coin_list and os.path.exists("SUPPORTED_COIN_LIST"):
        with open("SUPPORTED_COIN_LIST") as rfh:
            for line in rfh:
                line = line.strip()
                if not line or line.startswith("#") or line in supported_coin_list:
                    continue
                supported_coin_list.append(line)
                SUPPORTED_COIN_LIST = supported_coin_list

    print(supported_coin_list)
