from requests import get

headers = {'Accept': 'application/json',
           'Content-Type': 'application/json',
           'User-Agent': 'coinbase/python/2.0'}

def get_spot_price(crypto_currency='ETH', currency='EUR'):
    r = get("https://api.coinbase.com/v2/prices/{}-{}/spot".format(crypto_currency, currency))
    return r.json()['data']['amount']

def get_buy_price(crypto_currency='ETH', currency='EUR'):
    r = get("https://api.coinbase.com/v2/prices/{}-{}/buy".format(crypto_currency, currency))
    return r.json()['data']['amount']

def get_sell_price(crypto_currency='ETH', currency='EUR'):
    r = get("https://api.coinbase.com/v2/prices/{}-{}/sell".format(crypto_currency, currency))
    return r.json()['data']['amount']
