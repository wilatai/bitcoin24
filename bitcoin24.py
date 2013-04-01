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

	#########################################################################
	#	Support methods
	#########################################################################

	def get_request(self, url):
		"""
		Makes a simple GET request to the URL provided. Returns a JSON result
		on HTTP status code 200. In other cases it will return either the 
		response object or, in case of an exception, None 
		"""
		try:
			resp = requests.get(url)
			if resp.status_code == 200:
				return resp.json()
			return resp			
		except requests.RequestException as e:
			print e.message
			return None

	def post_request(self, api_method, arg_params={}):
		"""
		Makes an API POST request using the provided parameters. Returns a
		JSON result on HTTP status code 200. In other cases it will return
		either the response object or, in case of an exception, None.
		"""

		params = {'user': self.API_USER,
				  'key':  self.API_KEY,
				  'api':  api_method}
		params.update(arg_params)

		try:
			resp = requests.post(url=API_URL, data=params)
			if resp.status_code == 200:
				return resp.json()
			return resp
		except requests.RequestException as e:
			print e.message
			return None

	##########################################################################
	#	Methods that do NOT require an API user + key
	##########################################################################

	def ticker(self, currency='EUR'):
		"""Returns the current ticker in either 'EUR' or 'USD'"""
		return self.get_request(url=TICKER_URL % currency)

	def orderbook(self, currency='EUR'):
		"""Returns the current order book in either 'EUR' or 'USD'"""
		return self.get_request(url=ORDERBOOK_URL % currency)

	##########################################################################
	#	Methods requiring an API user + key
	##########################################################################

	def account_balance(self):
		"""Returns the account balance"""
		return self.post_request('get_balance')

	def bitcoin_address(self):
		"""Returns the users Bitcoin address on Bitcoin-24.com"""
		return self.post_request('get_addr')

	def open_orders(self):
		"""Returns open orders"""
		return self.post_request('open_orders')

	def cancel_order(self, order_id):
		"""Cancels an order"""
		return self.post_request('cancel_order', {'id': order_id})

	def buy_btc(self, btc_amount, price_per_btc, currency='EUR'):
		"""Buys btc_amount of Bitcoin for price_per_btc per Bitcoin in the currency specified ('EUR' (default) or 'USD')"""
		return self.post_request('buy_btc', {'amount': btc_amount, 'price': price_per_btc, 'cur': currency})

	def sell_btc(self, btc_amount, price_per_btc, currency='EUR'):
		"""Sells btc_amount of Bitcoin for price_per_btc per Bitcoin in the currency specified ('EUR' (default) or 'USD')"""
		return self.post_request('sell_btc', {'amount': btc_amount, 'price': price_per_btc, 'cur': currency})

	def withdraw_btc(self, btc_amount, btc_address):
		"""Withdraws btc_amount of Bitcoin to Bitcoin address btc_address)"""
		return self.post_request('withdraw_btc', {'amount': btc_amount, 'address': btc_address})

	def trades(self):
		"""Returns the users trades in JSON format"""
		return self.post_request('trades_json')

if __name__ == '__main__':

	# Example usage
	btc24 = Bitcoin24('your_api_user_name', 'your_api_key')
	print btc24.ticker()
