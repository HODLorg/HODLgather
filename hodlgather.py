#! usr/bin/python3

# Calculates various figures about Bitcoin stash and investment goals

import time
import math
import requests

from matplotlib import pyplot as pp

from config.config import config


# Start price in eur at 2018-04-18
# Grow per day - 0.5 % for BDP (Mc Affees Big Dick Prediction)
def predicted_price(start_price=10000.00, start_timestamp=time.time(), daily_growth=0.005, timestamp=time.time() + 30 * 86400 * 12):
    ts_difference = timestamp - start_timestamp
    days = ts2days(ts_difference)
    predicted_price = start_price * math.pow(1 + daily_growth, days)

    return predicted_price


def ts2days(timestamp):
    days = timestamp / 60 / 60 / 24

    return days


def main():
    months = config['months']
    init_amount_btc =config['init_amount_btc']
    invested_amount_eur = config['invested_amount_eur']
    monthly_adding_eur = config['monthly_adding_eur']
    start_price = config['start_price']
    daily_growth = config['daily_growth'] / 100.0

    future_timestamp = time.time() + 30 * 86400 * months
    end_price = predicted_price(start_price=start_price, start_timestamp=time.time(), daily_growth=daily_growth, timestamp=future_timestamp)

    print("Start of simulation.")
    print("Price is {:2f} EUR / BTC".format(start_price))
    print("Invested {:2f} EUR.".format(invested_amount_eur))
    print("Holding {:3f} BTC.".format(init_amount_btc))
    print("Predicted price after {} monhts is {:2f} EUR / BTC.\n".format(months, end_price))

    amount_btc = init_amount_btc
    t = []
    y = []
    for i in range(months):
        month = i + 1
        future_timestamp = time.time() + 30 * 86400 * month
        predicted_price_eur = predicted_price(start_price=start_price, start_timestamp=time.time(), daily_growth=daily_growth, timestamp=future_timestamp)
        amount_btc += monthly_adding_eur / predicted_price_eur
        value_eur = amount_btc * predicted_price_eur
        invested_amount_eur += monthly_adding_eur
        gain_percent = (value_eur / invested_amount_eur - 1) * 100
        t.append(month)
        y.append(amount_btc)
        print("After {} months:".format(month))
        print("Price is {:2f} EUR / BTC".format(predicted_price_eur))
        print("Invested {:2f} EUR.".format(invested_amount_eur))
        print("Gathered {:3f} BTC (value {:2f}).".format(amount_btc, value_eur))
        print("Gained {:2f} %.\n".format(gain_percent))

    pp.plot(t, y)
    pp.show()


if __name__ == "__main__":
    main()
