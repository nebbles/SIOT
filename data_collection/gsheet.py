#!/usr/bin/python3
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
import sys


def get_document():
    """Wrapper for authenticating and returning a document object"""

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        os.path.join(sys.path[0], "google_credentials.json"), scope)

    gc = gspread.authorize(credentials)
    return gc.open_by_key("1LZsKVQDmauzADwlaHXeJy4nndVv-vmaXoD8lfbPoqQo")


def add_to_sheet(sheet_name, row):
    # TODO Function is deprecated due to get_document() and needs to be removed once dependents are updated.
    doc = get_document()
    doc.worksheet(sheet_name).append_row(row)


def get_sheet(sheet_name):
    """Wrapper function to simplify calls for all sheet data"""
    return get_document().worksheet(sheet_name).get_all_values()


if __name__ == "__main__":
    import time

    # TEST BEHAVIOUR TO CHECK IT IS FUNCTIONING PROPERLY
    for i in range(10):
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S')
        row = [cur_time, i]
        print("Adding to sheet: {}".format(row))
        add_to_sheet('TEST', row)
        time.sleep(1)
