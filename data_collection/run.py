#!/usr/bin/python3
from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'data_collection/credentials.json', scope)

gc = gspread.authorize(credentials)

doc = gc.open_by_key("1LZsKVQDmauzADwlaHXeJy4nndVv-vmaXoD8lfbPoqQo")

doc.worksheet('API-1').update_acell('C6', "test doc file string")

# Fetch a cell range
# cell_list = wks.range('A1:D7')
# print(cell_list)
