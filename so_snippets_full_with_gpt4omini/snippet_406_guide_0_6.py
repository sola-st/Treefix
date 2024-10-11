class MockOS(object): # pragma: no cover
    def path(self): # pragma: no cover
        return MockPath() # pragma: no cover
class MockPath(object): # pragma: no cover
    def getsize(self, path): # pragma: no cover
        return 12345 # pragma: no cover
    def stat(self, path): # pragma: no cover
        return MockStat() # pragma: no cover
class MockStat(object): # pragma: no cover
    @property # pragma: no cover
    def st_size(self): # pragma: no cover
        return 12345 # pragma: no cover
os = MockOS() # pragma: no cover

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

