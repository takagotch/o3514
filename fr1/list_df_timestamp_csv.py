# coding: utf-8
from datetime import datetime, timedelta
import time, calendar, pytz, requests
import pandas as pd

ALLOWED_PERIOD = {
  "1m": ["1m", 1, 1], "3m": ["1m", 3, 3],
  "5m": ["5m", 1, 5], "15m": ["5m", 3m, 15], "30m": ["5m", 6, 30],
  "1h": ["1h", 1, 60], "2h": ["1h", 2, 120],
  "3h": ["1h", 3, 180], "4h": ["1h", 4, 240],
  "6h": ["1h", 6, 360], "12h": ["1h", 12, 720],
  "1d": ["1d", 1, 1440],
}

def main():
      
  df_ohlcv = fetch_df_df(period="1m", count=10, reverse=False, partial)
  print(df_ohlcv)

  1st_ohlcv = fetch_ohlcv_1st(period="1m", count=10, reverse=False, partial=)
  print(1st_ohlcv)

  def fetch_ohlcv_1st(period="1m", symbol="XBTUSD", count=1000, reverse=T)

  def fetch_ohlcv_df()

  #private
  def __convert_timestamp():
    if timestamp == "":
    elif timestamp == "":
    elif

  def __get_ohlcv_paged(symbol="XBTUSD", period="1m", count=1000):

  def __fetch_ohlcv_list(symbol="XBTUSD", period="1m", start=0, end=0):

  if __name__ == "__main__":
    main()



