#!/usr/bin/python3

from os import path
import csv
import gsheet
from datetime import datetime as dt
from datetime import timedelta as td
from ansi import ansi
from pprint import pprint


def get_csv_data(name):
    file_data = []
    filename = path.join(path.dirname(path.abspath(__file__)), name)

    with open(filename, 'r') as f:
        csv_reader = csv.reader(f)

        for row in csv_reader:
            file_data.append(row)

    return file_data


def check_db(db, time_checks):
    # data structure that will store the result of the check
    report = {
        "unexpected": [],
        "missing": []
    }
    time_index = 0  # starts checking against the first expected time
    db_index = 1  # Starts at 1 to skip header row

    # pprint(db[4043:4048])

    while time_index < len(time_checks):

        try:
            cur_row = db[db_index]
        except IndexError:
            report['missing'].append(time_checks[time_index])
            time_index += 1
            continue

        cur_min = dt.fromisoformat(cur_row[0]).replace(second=0)

        # marker = time_checks[time_index]

        # if marker.hour == 21 and marker.day == 1:
        #     print(time_checks[time_index], db_index, cur_row)

        if time_checks[time_index] == cur_min:
            # ansi.printok("Success. CSV matches expected output for {} -> {}".format(TIME_MARK, cur_csv_row))
            db_index += 1
            time_index += 1

        elif time_checks[time_index] > cur_min:
            report['unexpected'].append(cur_row)
            db_index += 1

        elif time_checks[time_index] < cur_min:
            report['missing'].append(time_checks[time_index])
            time_index += 1

    return report


def main():
    # Set the start time for data collection
    time_mark = dt.fromisoformat('2018-12-23 20:30:00')
    print("Data collection start point manually set to: {}".format(time_mark))

    # Create a list of all the expected scheduled data points
    expected_times = []
    while time_mark <= dt.now():
        expected_times.append(time_mark)
        time_mark += td(seconds=60*3)

    # Get databases
    stocks_csv_data = get_csv_data("stocks.csv")
    stocks_gs_data = gsheet.get_sheet('API-STOCKS')

    weather_csv_data = get_csv_data("weather.csv")
    weather_gs_data = gsheet.get_sheet('API-WEATHER')

    # Check the databases against the expected scheduled times
    stocks_csv_report = check_db(stocks_csv_data, expected_times)
    stocks_gs_report = check_db(stocks_gs_data, expected_times)

    weather_csv_report = check_db(weather_csv_data, expected_times)
    weather_gs_report = check_db(weather_gs_data, expected_times)

    # Print the results out
    print("              TIME           ---------STOCKS--------   --------WEATHER--------")
    print("              TIME              CSV         GSHEET        CSV         GSHEET  ")
    print("       ===================   ==========   ==========   ==========   ==========")

    missing_count = 0
    stocks_csv_missing = 0
    stocks_gs_missing = 0
    weather_csv_missing = 0
    weather_gs_missing = 0
    for time in expected_times:
        status_width = 10
        stocks_csv_status = ansi.ok("OK".ljust(status_width))
        stocks_gs_status = ansi.ok("OK".ljust(status_width))
        weather_csv_status = ansi.ok("OK".ljust(status_width))
        weather_gs_status = ansi.ok("OK".ljust(status_width))

        stocks_csv_is_missing = time in stocks_csv_report['missing']
        stocks_gs_is_missing = time in stocks_gs_report['missing']
        weather_csv_is_missing = time in weather_csv_report['missing']
        weather_gs_is_missing = time in weather_gs_report['missing']

        if stocks_csv_is_missing:
            stocks_csv_status = ansi.error("MISSING".ljust(status_width))
            stocks_csv_missing += 1

        if stocks_gs_is_missing:
            stocks_gs_status = ansi.error("MISSING".ljust(status_width))
            stocks_gs_missing += 1

        if weather_csv_is_missing:
            weather_csv_status = ansi.error("MISSING".ljust(status_width))
            weather_csv_missing += 1

        if weather_gs_is_missing:
            weather_gs_status = ansi.error("MISSING".ljust(status_width))
            weather_gs_missing += 1

        if stocks_csv_is_missing or stocks_gs_is_missing or weather_csv_is_missing or weather_gs_is_missing:
            missing_count += 1
            print("{:4d}   {}   {}   {}   {}   {}".format(
                missing_count, time, stocks_csv_status, stocks_gs_status, weather_csv_status, weather_gs_status))

    print("       ===================   ==========   ==========   ==========   ==========\n")
    print("STOCKS  CSV: {} missing rows".format(len(stocks_csv_report['missing'])))
    print("             {} additional rows".format(len(stocks_csv_report['unexpected'])))
    print("      SHEET: {} missing rows".format(len(stocks_gs_report['missing'])))
    print("             {} additional rows".format(len(stocks_gs_report['unexpected'])))
    print("")
    print("WEATHER CSV: {} missing rows".format(len(weather_csv_report['missing'])))
    print("             {} additional rows".format(len(weather_csv_report['unexpected'])))
    print("      SHEET: {} missing rows".format(len(weather_gs_report['missing'])))
    print("             {} additional rows".format(len(weather_gs_report['unexpected'])))


if __name__ == "__main__":
    main()
