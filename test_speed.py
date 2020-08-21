# Test Speed of home broadband every x seconds and send metrics to InfluxDB
import speedtest
import logging
import json


# Initiating default log
logger = logging.getLogger('home-bot-speedtest')


# Test and return a dict of download and upload speed
def test_speed():
    logger.info('Testing speed...')
    servers = []
    logger.debug('Servers: %s', servers)
    threads = None
    logger.debug('Threads: %s', threads)

    speed_test = speedtest.Speedtest()
    speed_test.get_servers(servers)
    logger.debug('Getting best server...')
    speed_test.get_best_server()
    logger.info('Testing download speed...')
    speed_test.download(threads=threads)
    logger.info('Testing upload speed...')
    speed_test.upload(threads=threads)
    test_results = speed_test.results.dict()
    results_json = json.dumps(test_results, indent=2)
    logger.debug('Test complete: %s', results_json)
    return test_results
