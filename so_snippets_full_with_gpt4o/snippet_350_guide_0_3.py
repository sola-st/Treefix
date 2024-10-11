import types # pragma: no cover

def mock_addFun(*args, **kwargs): # pragma: no cover
    return sum(args) # pragma: no cover
module = types.ModuleType('b') # pragma: no cover
module.addFun = mock_addFun # pragma: no cover
sys.modules['b'] = module # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
from l3.Runtime import _l_
try:
    from .b import addFun
    _l_(12802)

except ImportError:
    pass

