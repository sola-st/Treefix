 # pragma: no cover

class MockB:# pragma: no cover
    def addFun(self):# pragma: no cover
        pass# pragma: no cover
# pragma: no cover
# pragma: no cover
sys.modules['.b'] = MockB # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
from l3.Runtime import _l_
try:
    from .b import addFun
    _l_(12802)

except ImportError:
    pass

