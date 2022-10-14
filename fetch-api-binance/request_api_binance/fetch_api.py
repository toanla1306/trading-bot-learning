import ccxt
from ccxt import exchanges

def request_ohlcv(exchange, pair_id):
    response = exchange.fetch_ohlcv(pair_id, timeframe='1m', limit=5)
    return response

# [str(index) for index in b])
# datetime.fromtimestamp(float(time)/1000)