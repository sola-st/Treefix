import csv # pragma: no cover

filename = 'dummy.csv' # pragma: no cover
with open(filename, 'w', encoding='utf16') as f: f.write('header1,header2\nvalue1,value2') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
from l3.Runtime import _l_
file = open('filename.csv', encoding="utf16")
_l_(976)

