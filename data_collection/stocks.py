#!/usr/bin/python3
from requests import get, codes
import json
from pprint import pprint
import time
import datetime
import gsheet
import sys
import os
import csv
import utils

# def call_api(url):
#     resp = get(url)
#     if resp.status_code != codes['ok']:
#         raise RuntimeError(
#             "Response returned error {} for URL: {}".format(resp.status_code, url))
#     else:
#         return json.loads(resp.text)


def get_quote(key, symbol):
    quote = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={apikey}".format(
        symbol=symbol, apikey=key)

    return utils.call_api(quote)


def get_currency(key, from_currency, to_currency):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={fc}&to_currency={tc}&apikey={apikey}".format(
        fc=from_currency, tc=to_currency, apikey=key)

    return utils.call_api(url)


if __name__ == "__main__":
    # Collect API credentials from external JSON file
    with open(os.path.join(sys.path[0], "credentials.json")) as key_file:
        creds = json.load(key_file)

    # Get the current time on server
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S')

    # Get the current price for FTSE 100
    quote_data = get_quote(creds['alpha_vantage']['key'], "^FTSE")
    ftse_price = quote_data['Global Quote']['05. price']

    # Get the current exchange rate
    currency_data = get_currency(creds['alpha_vantage']['key2'], "GBP", "USD")
    ex_rate = currency_data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    ex_time = currency_data['Realtime Currency Exchange Rate']['6. Last Refreshed']

    # Compile data into new spreadsheet row
    row = [cur_time, float(ftse_price), ex_time, float(ex_rate)]

    # Appending row to a CSV (as backup to Google Sheet)
    with open(os.path.join(sys.path[0], "stocks.csv"), 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    # Append new row to end of correct tab in Google Sheet
    gsheet.add_to_sheet('API-STOCKS', row)
