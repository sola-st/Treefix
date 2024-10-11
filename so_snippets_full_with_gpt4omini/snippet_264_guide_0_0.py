import csv # pragma: no cover
import os # pragma: no cover

filename = 'test.csv' # pragma: no cover
with open(filename, 'w', encoding='utf16', newline='') as f: csv.writer(f).writerow(['header1', 'header2']) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
from l3.Runtime import _l_
file = open('filename.csv', encoding="utf16")
_l_(976)

