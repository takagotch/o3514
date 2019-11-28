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
    }, columns = ["timestamp", "oepn", "high", "low", "close", "volume"])



