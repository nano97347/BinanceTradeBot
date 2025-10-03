import configparser
import os

CFG_FL_NAME = "user.cfg"

class Config:
    def __init__(self):
        if not os.path.exists(CFG_FL_NAME):
            print("No configuration file (user.cfg) found!")
