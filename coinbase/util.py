import datetime

def get_timestamp():
    t = datetime.datetime.now()
    print(t)
    return t

def get_timestamp_YmdHMS_as_str():
    t = get_timestamp()
    return t.strftime("%Y-%m-%d %H:%M:%S")

def timestamp_to_YmdHMS_str(t):
    return t.strftime("%Y-%m-%d %H:%M:%S")

def timestamp_to_Y_m_d_str(t):
    return t.strftime("%Y_%m_%d")
