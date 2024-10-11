import sys # pragma: no cover
from types import ModuleType # pragma: no cover
import builtins # pragma: no cover

mock_module = ModuleType('b') # pragma: no cover
def addFun(): pass # pragma: no cover
mock_module.addFun = addFun # pragma: no cover
sys.modules['b'] = mock_module # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
from l3.Runtime import _l_
try:
    from .b import addFun
    _l_(12802)

except ImportError:
    pass

