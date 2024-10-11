import os # pragma: no cover
from pathlib import Path # pragma: no cover

class MockPath:  # Mock class for pathlib.Path # pragma: no cover
    def __init__(self, path): # pragma: no cover
        self.path = path # pragma: no cover
    def stat(self): # pragma: no cover
        return type('MockStat', (object,), {'st_size': 42})()  # Mock stat result # pragma: no cover
os.path = type('Mock', (object,), {'getsize': lambda path: 42})()  # Mock os.path.getsize # pragma: no cover
os.stat = lambda path: type('MockStat', (object,), {'st_size': 42})()  # Mock os.stat # pragma: no cover
Path = MockPath  # Assign MockPath to Path # pragma: no cover

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

