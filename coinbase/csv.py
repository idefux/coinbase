from util import timestamp_to_YmdHMS_str

def log_spot_buy_sell_price(filename, timestamp, spot, buy, sell):
    with open(filename, 'a+') as f:
        f.write(u";".join([timestamp_to_YmdHMS_str(timestamp), spot, buy, sell]))
        f.write(u"\n")
