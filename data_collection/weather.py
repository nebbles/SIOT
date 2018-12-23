#!/usr/bin/python3
from requests import get
import json
from pprint import pprint
import gsheet
import time
import csv
import sys
import os


def get_darksky_weather(key, location):
    api_url = "https://api.darksky.net/forecast/{}/{loc[0]:},{loc[1]:}?exclude=minutely,hourly,daily&units=si".format(
        key, loc=location)
    resp = get(api_url)
    return json.loads(resp.text)


if __name__ == "__main__":
    # Collect API credentials from external JSON file
    with open(os.path.join(sys.path[0], "credentials.json")) as key_file:
        creds = json.load(key_file)

    # Get the current time on server
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S')

    dbde = ("51.497999", "-0.174511")  # Lat, Long Dyson Building
    london = ("51.506321", "-0.12714")  # Lat, Long for London

    # Get current weather data for location
    data = get_darksky_weather(creds['dark_sky'], dbde)

    data_time = data['currently']['time']  # Extract time from API call
    ds_time = time.strftime('%Y-%m-%d %H:%M:%S',
                            time.gmtime(int(data_time)))  # Format time to ISO

    # Extract key values from weather data
    temp = data['currently']['apparentTemperature']
    precip = data['currently']['precipProbability']
    precip_intensity = data['currently']['precipIntensity']
    hum = data['currently']['humidity']
    pressure = data['currently']['pressure']
    storm_dist = data['currently']['nearestStormDistance']

    # Compile data into new spreadsheet row
    row = [cur_time, ds_time, temp, precip,
           precip_intensity, hum, pressure, storm_dist]
    # row = [cur_time,cur_time,0,0] # FOR DEBUGGING PURPOSES

    # Appending row to a CSV (as backup to Google Sheet)
    with open(os.path.join(sys.path[0], "weather.csv"), 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

    # Append new row to end of correct tab in Google Sheet
    gsheet.add_to_sheet('API-WEATHER', row)
