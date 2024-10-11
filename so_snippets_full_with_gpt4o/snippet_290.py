# Extracted from https://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments
parser.add_argument('dir', nargs='?', default=os.getcwd())

import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store_true')
_StoreTrueAction(option_strings=['-v'], dest='v', nargs=0, const=True, default=False, type=None, choices=None, help=None, metavar=None)
parser.add_argument('dir', nargs='?', default=os.getcwd())
_StoreAction(option_strings=[], dest='dir', nargs='?', const=None, default='/home/vinay', type=None, choices=None, help=None, metavar=None)
parser.parse_args('somedir -v'.split())
Namespace(dir='somedir', v=True)
parser.parse_args('-v'.split())
Namespace(dir='/home/vinay', v=True)
parser.parse_args(''.split())
Namespace(dir='/home/vinay', v=False)
parser.parse_args(['somedir'])
Namespace(dir='somedir', v=False)
parser.parse_args('somedir -h -v'.split())
usage: [-h] [-v] [dir]

positional arguments:
  dir

optional arguments:
  -h, --help  show this help message and exit
  -v

