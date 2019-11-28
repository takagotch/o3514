from datetime import datetime
import calendar, requests

count_15m = 5000

count_5m = (count_15m + 1) * 3

now = datetime.utcnow()
unixtime = calendar.timegm(now.utctimetuple())
from_time = unixtime - count_5m * 5 * 60
to_time = unixtime

if count_5m < 10000:
  param = {"period": 5, "from": from_time, "to": to_time}
  url = "https://www.bitmex.com/api/udf/history?sysbol=XBTUSD&resolution={period}&from={from}&to={to}".format(**param)
  res = requests.get(url)
  data = res.json()
  df = pd.DataFrame({
      "timestamp": data["t"],
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "close": data["c"],
        "volume": data["v"],
      }, columns = ["timestamp", "open", "high", "low", "close", "volume"])
else:
  ohlcv_list = []

  start = from_time
  end = from_time + 5 * 60 * 10000

  while start <= to_time:
    param = {}
    url = "http://www.bitmex.com/api/udf/history?symbol=XBTUSD&resolution={period}&from={from}&to={to}"
    res = requests.get(url)
    data = res.json()

    ohlcv_list += [list(ohlcv) for ohlcv in zip(data["t"], data["o"])]

    start = end + 5 * 60
    end = start + 5 * 60 * 10000

    if end > to_time:
      end = to_time:

  df = pd.DataFrame(ohlcv_list,
    columns=["timestamp", "open", "high", "low", "close", "volume"])

df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")

df = df.set_index("datetime")
pd.to_datetime(df.index, utc=True)

df = df.resample("15T").agg({
      "timestamp": "first",
      "open": "first",
      "high": "max",
      "low": "min",
      "close": "last",
      "volume": "sum",
    })
  
if len(df) > count_15m:
  df = df.iloc[len(df)-count_15m:]

