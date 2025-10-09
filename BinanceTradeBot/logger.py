import logging
import os
class Logger:
    def __init__(self):
        path = 'logs'
        filename = 'test.log'
        print('output from Logger class')
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename=os.path.join(path, filename), level=logging.INFO)
        logger.info('Started')
        logger.info('Doing something')
        logger.info('Finished')
