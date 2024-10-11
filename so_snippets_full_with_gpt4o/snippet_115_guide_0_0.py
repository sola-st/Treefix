import sys # pragma: no cover
import types # pragma: no cover

module_name = 'foo' # pragma: no cover
foo = types.ModuleType(module_name) # pragma: no cover
sys.modules[module_name] = foo # pragma: no cover
foo.some_name = 'some_value' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/44834/what-does-all-mean-in-python
from l3.Runtime import _l_
try:
    from foo import *
    _l_(13015)

except ImportError:
    pass

__all__ = ('some_name',)
_l_(13016)

