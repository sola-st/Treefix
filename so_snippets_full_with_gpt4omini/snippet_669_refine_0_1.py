import types # pragma: no cover

mymodule = types.ModuleType('mymodule') # pragma: no cover

import types # pragma: no cover

mymodule = types.ModuleType('mymodule') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/684171/how-to-re-import-an-updated-package-while-in-python-interpreter
from l3.Runtime import _l_
del mymodule
_l_(73)
try:
    import mymodule
    _l_(75)

except ImportError:
    pass

