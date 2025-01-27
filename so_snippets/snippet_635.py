# Extracted from https://stackoverflow.com/questions/8259001/python-argparse-command-line-flags-without-arguments
import argparse
parser = argparse.ArgumentParser('parser-name')
parser.add_argument("-f","--flag",action="store_true",help="just a flag argument")

python3 script.py -f

args = parser.parse_args()
print(args.f)

true

