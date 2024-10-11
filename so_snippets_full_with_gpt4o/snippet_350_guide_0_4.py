import sys # pragma: no cover
from types import ModuleType # pragma: no cover

b = ModuleType('b') # pragma: no cover
sys.modules['b'] = b # pragma: no cover
def addFun(x, y): return x + y # pragma: no cover
b.addFun = addFun # pragma: no cover
sys.modules['.b'] = b # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
from l3.Runtime import _l_
try:
    from .b import addFun
    _l_(12802)

except ImportError:
    pass

