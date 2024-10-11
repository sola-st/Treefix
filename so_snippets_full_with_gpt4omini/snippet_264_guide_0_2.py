import pandas as pd # pragma: no cover
import os # pragma: no cover

filename = 'test.csv' # pragma: no cover
if not os.path.exists(filename): # pragma: no cover
    with open(filename, 'w', encoding='utf8') as f: # pragma: no cover
        f.write('column1,column2\nvalue1,value2') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
from l3.Runtime import _l_
file = open('filename.csv', encoding="utf16")
_l_(976)

