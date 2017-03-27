Station Simulator
=================

*A script for generating large station CSVs fast*

Copyright 2017 RPS Group Plc

See LICENSE for details


Installation
============

To install using pip::

    pip install station-simulator


Usage
=====

::

    usage: station-simulator [-h] [-n STATION_NAME] [-s START] [-e END] output

    Generate a fake CSV of station data

    positional arguments:
      output                Output file

    optional arguments:
      -h, --help            show this help message and exit
      -n STATION_NAME, --station-name STATION_NAME
                            Name of station
      -s START, --start START
                            Start Date
      -e END, --end END     End Date

Examples::

    station-simulator test.csv

    station-simulator -n Example1 --start 2001-01-01 --end 2010-01-01 output.csv
