# Extracted from https://stackoverflow.com/questions/7427101/simple-argparse-example-wanted-1-argument-3-results
import argparse

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('-h', '--help', action='help',
                help='To run this script please provide two arguments')
parser.parse_args()

usage: test.py [-h]

optional arguments:
  -h, --help  To run this script please provide two arguments

