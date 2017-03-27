#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
dubai_generator/cli.py
'''
from argparse import ArgumentParser
from datetime import datetime, timedelta
import random
import sys
import csv
import arrow


def dateparse(date_str):
    '''
    Returns a datetime string parsed from an ISO-8601 input

    :param str date_str: An ISO-8601 string
    '''
    if date_str.endswith('+00'):
        date_str = date_str.replace('+00', 'Z')
    arrow_obj = arrow.get(date_str)
    return arrow_obj.to('utc').naive


def generate_csv(output, station_name, start_date, end_date):
    '''
    Writes a bunch of random data to output

    :param str output: Path to file to write
    :param str station_name: Name of the station as it should appear in CSV file
    :param datetime start_date: Start Date
    :param datetime end_date: End Date
    '''
    current_date = start_date
    with open(output, 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Station', 'Date/Time', 'Conductivity (S/m-1)',
                             'Temperature (deg_C)', 'Pressure (mbar)'])

        while current_date < end_date:
            row = generate_row(station_name, current_date)
            csv_writer.writerow(row)

            current_date += timedelta(hours=1)


def generate_row(station_name, date):
    '''
    Returns a row of data

    :param str station_name: Name of the station
    :param datetime date: Date for row
    '''
    if random.random() < 0.1:
        cond = float('nan')
    else:
        cond = random.random() + 1.0  # 1.0 - 2.0

    if random.random() < 0.1:
        temp = float('nan')
    else:
        temp = 7 * random.random() + 10.0
    if random.random() < 0.1:
        press = float('nan')
    else:
        press = random.random() + 3

    return (station_name, date.isoformat(), cond, temp, press)


def main():
    '''
    Generate a fake CSV of station data
    '''
    parser = ArgumentParser(description=main.__doc__)
    parser.add_argument('-n', '--station-name', default='DUBAL', help='Name of station')
    parser.add_argument('-s', '--start', default='2017-01-01', help='Start Date')
    parser.add_argument('-e', '--end',
                        default=datetime.utcnow().strftime('%Y-%m-%d'), help='End Date')
    parser.add_argument('output', help='Output file')
    args = parser.parse_args()

    start_date = dateparse(args.start)
    end_date = dateparse(args.end)
    generate_csv(args.output, args.station_name, start_date, end_date)
    return 0


if __name__ == '__main__':
    sys.exit(main())
