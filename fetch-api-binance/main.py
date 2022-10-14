import ccxt
from ccxt import exchanges
import time
from datetime import datetime
from request_api_binance.fetch_api import request_ohlcv
# from request_api_binance.connection_database import insert_data

exchange = ccxt.binance ({
    'rateLimit': 1,  # unified exchange property
    'headers': {
        'YOUR_CUSTOM_HTTP_HEADER': 'YOUR_CUSTOM_VALUE',
    },
    'options': {
        'adjustForTimeDifference': True,  # exchange-specific option
    }
})

start = time.time()
pair_id = 'NEAR/USDT'
responses = request_ohlcv(exchange, pair_id)
print(time.time() - start)
for response in responses:
    response = [str(index) for index in response]
    # insert_data(response)
    response[0] = str(datetime.fromtimestamp(float(response[0])/1000))
    response.insert(0, pair_id)
    print(tuple(response))
print(time.time() - start)
