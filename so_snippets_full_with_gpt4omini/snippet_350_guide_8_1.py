import sys # pragma: no cover

class MockModule: pass # pragma: no cover
sys.modules['.b'] = MockModule() # pragma: no cover
sys.modules['.b'].addFun = lambda: 'Mock function executed' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
from l3.Runtime import _l_
try:
    from .b import addFun
    _l_(3288)

except ImportError:
    pass

