import sys # pragma: no cover

class YourClass: pass # pragma: no cover
sys.modules['.YourClass'] = YourClass # pragma: no cover
class YourClassParentDir: pass # pragma: no cover
YourClassParentDir.YourClass = YourClass # pragma: no cover
sys.modules['YourClassParentDir'] = YourClassParentDir # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4534438/typeerror-module-object-is-not-callable
from l3.Runtime import _l_
try:
    from .YourClass import YourClass
    _l_(462)

except ImportError:
    pass
try:
    from YourClassParentDir import YourClass
    _l_(464)

except ImportError:
    pass

