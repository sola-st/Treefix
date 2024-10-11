import os # pragma: no cover
from pathlib import Path # pragma: no cover

class Mock: pass # pragma: no cover
os.path = Mock() # pragma: no cover
os.path.getsize = lambda path: 1000 # pragma: no cover
os.stat = lambda path: Mock() # pragma: no cover
Path = Mock() # pragma: no cover
Path.stat = lambda self: Mock() # pragma: no cover

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

