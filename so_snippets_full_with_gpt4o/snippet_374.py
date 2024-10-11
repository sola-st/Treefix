# Extracted from https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse
#!/usr/local/bin/python3.6

from argparse import ArgumentParser

description = 'testing for passing multiple arguments and to get list of args'
parser = ArgumentParser(description=description)
parser.add_argument('-i', '--item', action='store', dest='alist',
                    type=str, nargs='*', default=['item1', 'item2', 'item3'],
                    help="Examples: -i item1 item2, -i item3")
opts = parser.parse_args()

print("List of items: {}".format(opts.alist))

python3.6 temp_agrs1.py -i item5 item6 item7
List of items: ['item5', 'item6', 'item7']

python3.6 temp_agrs1.py -i item10
List of items: ['item10']

python3.6 temp_agrs1.py
List of items: ['item1', 'item2', 'item3']

