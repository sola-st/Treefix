import os # pragma: no cover

filename = 'testfile.txt' # pragma: no cover
os = type('MockOS', (object,), {'remove': lambda x: None})() # pragma: no cover

import os # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
from l3.Runtime import _l_
try:
    _l_(1154)

    os.remove(filename)
    _l_(1151)
except FileNotFoundError:
    _l_(1153)

    pass
    _l_(1152)

