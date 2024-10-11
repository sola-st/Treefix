import csv # pragma: no cover

filename = 'sample.csv' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
from l3.Runtime import _l_
file = open('filename.csv', encoding="utf16")
_l_(976)

