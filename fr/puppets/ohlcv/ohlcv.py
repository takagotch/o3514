
import numpy as npm
import pandas as pd

from puppeteer import Puppeteer

class Puppet(Puppeteer):
  _exchange = None
  _logger = None
  _config = None
  _discord = None
  _name = 'ohlcv'

  def __init__(self, Puppeteer):
    self._exchange = Puppeteer._exchange
    self._logger = Puppeteer._logger
    self._config = Puppeteer._config
    self._discord = Puppeteer._discord

  def run(self, ticker, orderbook, position, balance, candle):

    df_ohlcv1m = self.get_candleDF(candle)

    self._logger.debug(df_ohlcv1m)

    df_ohlcv15m = self.change_candleDF(df_ohlcv1m, '15m')

    self._logger.debug(df_ohlcv15m)

  # DataFrame
  #  params:
  #     candle:
  #  return:
  #      df:
  def get_candleDF(self, candle):
    df = pd.DataFrame(candle,
      columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    df['timestamp'] = pd.to_datetime(df['timestamp'], uint='ms')
    df = df.set_index('timestamp')

    return df

  def change_candleDF(self, ohlcv, resolution='1m'):
    """
    AS 年　年初
    A　年　年末
    MS 月　月初
    M　月　月末
    W　週　日曜
    D　日　0時
    H　時  0分
    T　分  0秒
    S  秒
    """

    """
    min 最小
    max
    sum
    average
    first
    last
    interpolate 補間
    """

    period = {
      '1m' : '1T',
      '3m' : '3T',
      '5m' : '5T',
      '15m' : '15T',
      '30m' : '30T',
      '1h' : '1H',
      '2h' : '2H',
      '3h' : '3H',
      '4h' : '4H',
      '6h' : '6H',
      '12h' : '12H',
      '1d' : '1D',
      '3d' : '3D',
      '1w' : '1W',
      '2w' : '2W',
      '1M' : '1M',
    }

    if resolution not in period.keys():
      return None

    df = pd.concat([ohlcv[['open', 'high', 'low', 'close']].resample(period[resolution], label='left', closed='left').agg({'open': 'first', 'high': 'max', 'low': 'min', 'close': 'last'}),
        ohlcv['volume'].resample(period[resolution], label='left', closed='left').sum()],
        axis=1
      )

    return df


