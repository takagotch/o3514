import urllib3
import json
import datetime
import time

urllib3.disable_warnings()

PERIOD = 60

SIZE = 10

SLEEP_T = 1

HTTP = urllib3.PoolManager()

def getOHLCV(http, start, period):
  url = 'https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc?after=' + str(start) + '&periods=' + str(period)

  resp = json.loads(http.request('GET', url).data.decode('utf-8'))['result'][str(period)]

  return resp

if __name__ == '__main__':
  while True:
    try:
      start = int(time.time()) - PERIOD * SIZE

      resp = getOHLCV(HTTP, start, PERIOD)

      print('---')
      print('date time , open , high , low , close, volume ')
      print('---')
      for r in resp:
        print(str(datetime.datetime.fromtimestamp(r[0])) + ", " + str(r[1]) + ", " + str(r[2]) + ", " + str(r[3]) + ", " + str(r[4]) + ", " + str(r[5]) + ", " + str(r[6]))
    except Exception as e:
        print("exception: ", e.args)

    time.sleep(SLEEP_T)

