import sys # pragma: no cover
import types # pragma: no cover

module_name = 'b' # pragma: no cover
addFun = lambda x, y: x + y # pragma: no cover
module = types.ModuleType(module_name) # pragma: no cover
setattr(module, 'addFun', addFun) # pragma: no cover
sys.modules['.' + module_name] = module # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20309456/how-do-i-call-a-function-from-another-py-file
from l3.Runtime import _l_
try:
    from .b import addFun
    _l_(12802)

except ImportError:
    pass

