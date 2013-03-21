##############################################################################
#
# A Python implementation of the Bitcoin24 API
#
# API Documentation & References used:
#
# https://bitcoin-24.com/user_api
# http://pastebin.com/xckVpDrS
#
# Developed by: https://github.com/wilatai
# [ 1HgT6WfriEpEwqCfpGWLNSeZUHHbYCwnEs ]
#
##############################################################################

# Uses Requests module '>= 1.1.0'
import requests

# URLs
API_URL       = 'https://bitcoin-24.com/api/user_api.php'
TICKER_URL    = 'https://bitcoin-24.com/api/%s/ticker.json'
ORDERBOOK_URL = 'https://bitcoin-24.com/api/%s/orderbook.json'

class Bitcoin24:

	def __init__(self, api_user='', api_key=''):
		self.API_USER = api_user
		self.API_KEY  = api_key

	##########################################################################
	#	Methods that do NOT require an API user + key
	##########################################################################

	def ticker(self, currency='EUR'):
		"""Returns the current ticker in either 'EUR' or 'USD'"""
		resp = requests.get(url=TICKER_URL % currency)
		if resp.status_code == 200:
			return resp.json()
		return resp

	def orderbook(self, currency='EUR'):
		"""Returns the current order book in either 'EUR' or 'USD'"""
		resp = requests.get(url=ORDERBOOK_URL % currency)
		if resp.status_code == 200:
				return resp.json()
		return resp

	##########################################################################
	#	Methods requiring an API user + key
	##########################################################################

	def request(self, api_method, arg_params={}):
		"""Makes an API request using the provided parameters"""

		params = {'user': self.API_USER,
				  'key':  self.API_KEY,
				  'api':  api_method}
		params.update(arg_params)

		resp = requests.post(url=API_URL, data=params)

		if resp.status_code == 200:
			return resp.json()
		return resp

	def account_balance(self):
		"""Returns the account balance"""
		return self.request('get_balance')

	def bitcoin_address(self):
		"""Returns the users Bitcoin address on Bitcoin-24.com"""
		return self.request('get_addr')

	def open_orders(self):
		"""Returns open orders"""
		return self.request('open_orders')

	def cancel_order(self, order_id):
		"""Cancels an order"""
		return self.request('cancel_order', {'id': order_id})

	def buy_btc(self, btc_amount, price_per_btc, currency='EUR'):
		"""Buys btc_amount of Bitcoin for price_per_btc per Bitcoin in the currency specified ('EUR' (default) or 'USD')"""
		return self.request('buy_btc', {'amount': btc_amount, 'price': price_per_btc, 'cur': currency})

	def sell_btc(self, btc_amount, price_per_btc, currency='EUR'):
		"""Sells btc_amount of Bitcoin for price_per_btc per Bitcoin in the currency specified ('EUR' (default) or 'USD')"""
		return self.request('sell_btc', {'amount': btc_amount, 'price': price_per_btc, 'cur': currency})

	def withdraw_btc(self, btc_amount, btc_address):
		"""Withdraws btc_amount of Bitcoin to Bitcoin address btc_address)"""
		return self.request('withdraw_btc', {'amount': btc_amount, 'address': btc_address})

	def trades(self):
		"""Returns the users trades in JSON format"""
		return self.request('trades_json')

if __name__ == '__main__':

	# Example usage
	btc24 = Bitcoin24('your_api_user_name', 'your_api_key')
	print btc24.ticker()