import pandas as pd # pragma: no cover

filename = 'test.csv' # pragma: no cover
pd.DataFrame({'Column1': [1, 2], 'Column2': ['A', 'B']}).to_csv(filename, encoding='utf16', index=False) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
from l3.Runtime import _l_
file = open('filename.csv', encoding="utf16")
_l_(976)

