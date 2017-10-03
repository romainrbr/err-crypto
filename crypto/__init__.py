import json
import requests
from errbot import BotPlugin, botcmd

class Example(BotPlugin):
	"""
	Show the value of any known cryptocurrency based on Cryptocompare.com
	"""

	@botcmd  # flags a command
	def crypto(self, msg, args):  # a command callable with !tryme
		"""
		crypto_name
		"""
		r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=USD' % (args.upper()))
		if 'Response' in r.json():
			return "This crypto is not listed"
		else:
			return "%s$" % (r.json()['USD'])
