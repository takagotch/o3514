#
# period = "1m" // 1m, 3m, 5m, 15m, 30m, 1h, 2h, 3h, 4h, 6h, 12h, 1d, 1mth, 1y
# symbol = "BTCUSD" 
# count = 1000
# reverse = True // T/F
# partial = False // T/F
# tstype = "UTMS" // UTMS, UTS, DT, STMS
#
# DateFrame : [[timestamp, oepn, high, low, close, volume], ...]
# List :      ...
#
# 1st_ohlcv = fetch_ohlcv_1st(period="15m", count=1000, tstype="DT")
# df_ohlcv = fetch_ohlcv_df(period="5m", count=1000, partial=True)

def fetch_ohlvc_1st(period="1m", symbol="XBTUSD", count=1000,
        reverse=True, partial=False, tstype="UTMS"):

def fetch_ohlcv_df(period="1m", symbol="BTCUSD", count=1000,
        reverse=True, partial=False, tstype="UTS")


