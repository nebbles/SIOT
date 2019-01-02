#!/usr/bin/python3
import json
import gsheet
import time
import csv
import sys
import os
import utils
import traceback


def get_darksky_weather(key, location):
    api_url = "https://api.darksky.net/forecast/{apikey}/{loc[0]:},{loc[1]:}?exclude=minutely,hourly,daily&units=si".format(
        apikey=key, loc=location)

    return utils.call_api(api_url)


if __name__ == "__main__":
    try:
        # Collect API credentials from external JSON file
        with open(os.path.join(sys.path[0], "credentials.json")) as key_file:
            creds = json.load(key_file)

        # Get the current time on server
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S')
        print("="*80)
        print("{}   Collecting data...".format(cur_time))

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

        print("{}   Done.".format(time.strftime('%Y-%m-%d %H:%M:%S')))

    except:
        tb = traceback.format_exc()
        print(tb)
        utils.send_email(
            "An exception was caught when running the script.\n\n{}".format(tb))
