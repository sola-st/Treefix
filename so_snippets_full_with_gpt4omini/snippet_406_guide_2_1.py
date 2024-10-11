import os # pragma: no cover
from pathlib import Path # pragma: no cover

class MockStat:  # Mock class to simulate os.stat result # pragma: no cover
    def __init__(self): # pragma: no cover
        self.st_size = 1234  # Mocked file size value # pragma: no cover
 # pragma: no cover
def mock_getsize(path):  # Mock function to simulate os.path.getsize # pragma: no cover
    return 1234 # pragma: no cover
 # pragma: no cover
os.path = type('MockPath', (object,), {'getsize': mock_getsize})()  # Creating a mock os.path # pragma: no cover
os.stat = lambda path: MockStat()  # Mocking os.stat # pragma: no cover
Path = lambda path: type('MockPath', (object,), {'stat': lambda self: MockStat()})()  # Mocking pathlib.Path # pragma: no cover

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

