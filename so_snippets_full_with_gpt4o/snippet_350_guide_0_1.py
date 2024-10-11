import sys # pragma: no cover
import types # pragma: no cover

sys.modules['__main__.b'] = types.ModuleType('b') # pragma: no cover
def addFun(a, b): return a + b # pragma: no cover
setattr(sys.modules['__main__.b'], 'addFun', addFun) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
from l3.Runtime import _l_
try:
    from .b import addFun
    _l_(12802)

except ImportError:
    pass

