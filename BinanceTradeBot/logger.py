import logging
class Logger:
    def __init__(self):
        print('output from Logger class')
        logger = logging.getLogger(__name__)
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logger.info('Started')
        logger.info('Doing something')
        logger.info('Finished')
