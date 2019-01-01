#!/usr/bin/python3

from os import path
import csv
import gsheet
from datetime import datetime as dt
from datetime import timedelta as td
from ansi import ansi


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

    while time_index < len(time_checks):

        try:
            cur_row = db[db_index]
        except IndexError:
            report['missing'].append(time_checks[time_index])
            time_index += 1
            continue

        cur_min = dt.fromisoformat(cur_row[0]).replace(second=0)

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
    csv_data = get_csv_data("stocks.csv")
    gs_data = gsheet.get_sheet('API-STOCKS')

    # Check the databases against the expected scheduled times
    csv_report = check_db(csv_data, expected_times)
    gs_report = check_db(gs_data, expected_times)

    # Print the results out
    print("              TIME              CSV         GSHEET ")
    print("       ===================   ==========   ==========")

    missing_count = 0
    csv_missing = 0
    gs_missing = 0
    for time in expected_times:
        status_width = 10
        csv_status = ansi.ok("OK".ljust(status_width))
        gs_status = ansi.ok("OK".ljust(status_width))

        csv_is_missing = time in csv_report['missing']
        gs_is_missing = time in gs_report['missing']

        if csv_is_missing:
            csv_status = ansi.error("MISSING".ljust(status_width))
            csv_missing += 1

        if gs_is_missing:
            gs_status = ansi.error("MISSING".ljust(status_width))
            gs_missing += 1

        if csv_is_missing or gs_is_missing:
            missing_count += 1
            print("{:4d}   {}   {}   {}".format(
                missing_count, time, csv_status, gs_status))

    print("       ===================   ==========   ==========\n")
    pc_missing = len(csv_report['missing']) / len(expected_times) * 100
    print("There are {} missing rows from CSV ({:2.0f}%)".format(
        len(csv_report['missing']), pc_missing))
    print("There are {} unexpected rows from CSV".format(
        len(csv_report['unexpected'])))
    print("")
    print("There are {} missing rows from GSheet".format(
        len(gs_report['missing'])))
    print("There are {} unexpected rows from GSheet".format(
        len(gs_report['unexpected'])))


if __name__ == "__main__":
    main()
