from datetime import datetime
import calendar, requests

now = datetime.utcnow()

unixtime = calendar.timegm(now.utctimetuple())

since = unixtime - 60 * 60

param = {"period": 5, "from": since, "to": unixtime}
url = "https://www.bitmex.com/api/udf/history?symbol=XBTUSD&resolution={ xxx }"
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


