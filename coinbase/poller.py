from time import sleep

from coinbase_api import get_spot_price, get_buy_price, get_sell_price
from csv import log_spot_buy_sell_price
from util import get_timestamp, timestamp_to_Y_m_d_str

def poll():
    while(True):
        try:
            timestamp = get_timestamp();

            filename = u"data/coinbase_prices_{}".format(timestamp_to_Y_m_d_str(timestamp))

            spot = get_spot_price()
            buy = get_buy_price()
            sell = get_sell_price()

            log_spot_buy_sell_price(filename, timestamp, spot, buy, sell)

            sleep(60) # 1 minute

        except Exception as e:
            print(e)

if __name__ == "__main__":
    poll()
