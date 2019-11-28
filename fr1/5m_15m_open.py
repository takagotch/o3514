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



