const asciichart = require ('asciichart')
const asTable = require ('as-table')
const log = require ('ololog').configure ({ locate: false })

require ('ansicolor').nice

export const ohlcv = async (exchange) => {
  
  const index = 4
  const ohlcv = await exchange.fetchOHLCV('BTC/USD', '1h')
  const lastPrice = ohlcv[ohlcv.length - 1][index]
  const series = ohlcv.slice(-80).map (x => x[index])
  const bitcoinRate = ('＄= $').green
  const chart = asciichart.plot (series, { height: 15, padding: '
  log.yello ("\n" + chart, bitcoinRate, "\n")'})
}



