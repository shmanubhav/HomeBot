# Test Speed of home broadband every x seconds and send metrics to InfluxDB
import speedtest


# Test and return a dict of download and upload speed
def test_speed():
    servers = []
    threads = None

    speed_test = speedtest.Speedtest()
    speed_test.get_servers(servers)
    speed_test.get_best_server()
    speed_test.download(threads=threads)
    speed_test.upload(threads=threads)
    speed_test.results.share()
    return speed_test.results.dict()
