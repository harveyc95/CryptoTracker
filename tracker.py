import urllib2
import json

class Currency ():
    def __init__(self, id):
        self.id = id
        self.history = []

class Transaction ():
    def __init__(self, timestamp, rate, amount, fee):
        self.timestamp = timestamp
        self.rate = rate
        self.amount = amount
        self.fee = fee
        
def getPrice(coin_id, currency_id):
    link = 'https://api.cryptonator.com/api/ticker/'
    link = link + "-".join([coin_id, currency_id])
    response = urllib2.urlopen(link)
    html = response.read()
    data = json.loads(html)
    return data["ticker"]["price"]

if __name__ == "__main__":
    CAD = Currency('CAD')
    BTC = Currency('ETH')
    BTC = Currency('BTC')