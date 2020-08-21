from test_speed import test_speed
import logging
import sys


# Initiating default log
def init_log():
    logging.basicConfig(level=logging.NOTSET)
    handle = "home-bot"
    logger_init = logging.getLogger(handle)
    logger_init.debug('Starting Log...')
    return logger_init
    

# Start HomeBot.
if __name__ == '__main__':
    logger = init_log()
    logger.info('Starting HomeBot...')
    logger.info('Running speedtest...')
    test_speed()
