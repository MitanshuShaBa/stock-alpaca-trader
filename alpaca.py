import alpaca_trade_api as tradeapi
from config import *

BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(base_url=BASE_URL, key_id=API_KEY, secret_key=SECRET_KEY)


def get_account():
    # Get our account information.
    account = api.get_account()

    # Check if our account is restricted from trading.
    if account.trading_blocked:
        print('Account is currently restricted from trading.')

    # Check how much money we can use to open new positions.
    print('${} is available as buying power.'.format(account.buying_power))

# Get our position in AAPL.
aapl_position = api.get_position('AAPL')

# Get a list of all of our positions.
portfolio = api.list_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))