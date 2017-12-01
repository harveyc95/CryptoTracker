import urllib2
import json

def getPrice(coin, currency):
    link = 'https://api.cryptonator.com/api/ticker/'
    link = link + "-".join([coin, currency])
    response = urllib2.urlopen(link)
    html = response.read()
    data = json.loads(html)
    return data["ticker"]["price"]

price = getPrice('eth', 'cad')
print price + ' ' + 'cad'
price = getPrice('btc', 'usd')
print price + ' ' + 'usd'