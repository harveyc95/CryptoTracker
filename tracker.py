import urllib2
import re

response = urllib2.urlopen('https://api.cryptonator.com/api/ticker/eth-cad')
html = response.read()

def getPrice(coin, currency):
	link = 'https://api.cryptonator.com/api/ticker/'
	link = "-".join([link+coin, currency])
	response = urllib2.urlopen(link)
	html = response.read()
	# print re.findall(r"[\w']+", html)
	result = html.replace('{',' ').replace('}',' ').replace('\"',' ').replace('\'',' ').replace(':',' ').replace(',',' ').split()
	print coin + ': ' + currency + ' $' + result[6]
	return result[6]

price = getPrice('eth', 'cad')
price = getPrice('btc', 'usd')