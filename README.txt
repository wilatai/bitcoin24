Bitcoin24 API in Python
-------------

This module is an implementation of the Bitcoin24 API in Python.

If you like this module, my address is 1HgT6WfriEpEwqCfpGWLNSeZUHHbYCwnEs
and donations are always appreciated ;-)


Implemented functionality
-------------

Not requiring an API user + key:

- Ticker:    Returns the current ticker in either EUR or USD
- Orderbook: Returns the current order book

Requiring an API user + key:

- Account balance:  Returns the account balance
- Bitcoin address:  Returns the users Bitcoin address on Bitcoin-24.com
- Open orders:      Returns open orders
- Cancel order:     Cancels an order 
- Buy Bitcoin:      Buys Bitcoin for a particular price in the the currency specified ('EUR' (default) or 'USD')
- Sell Bitcoin:     Sells Bitcoin for a particular price in the currency specified ('EUR' (default) or 'USD')
- Withdraw Bitcoin: Withdraws Bitcoins to another Bitcoin address