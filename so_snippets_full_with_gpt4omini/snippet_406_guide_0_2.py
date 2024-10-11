import os # pragma: no cover
from pathlib import Path # pragma: no cover

os = type('MockOS', (object,), {'path': type('MockPath', (object,), {'getsize': lambda x: 42})(), 'stat': lambda x: type('MockStatResult', (object,), {'st_size': 42})()})() # pragma: no cover
Path = type('MockPathLib', (object,), {'__init__': lambda self, path: None, 'stat': lambda self: type('MockStatResult', (object,), {'st_size': 42})()}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6591931/getting-file-size-in-python
from l3.Runtime import _l_
try:
    import os
    _l_(900)

except ImportError:
    pass
os.path.getsize('C:\\Python27\\Lib\\genericpath.py')
_l_(901)
try:
    import os
    _l_(903)

except ImportError:
    pass
os.stat('C:\\Python27\\Lib\\genericpath.py').st_size 
_l_(904) 
try:
    from pathlib import Path
    _l_(906)

except ImportError:
    pass
Path('C:\\Python27\\Lib\\genericpath.py').stat().st_size
_l_(907)

