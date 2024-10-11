import sys # pragma: no cover
import types # pragma: no cover

file_name = types.ModuleType('file_name') # pragma: no cover
sys.modules['file_name'] = file_name # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16869024/what-is-pycache
from l3.Runtime import _l_
try:
    import file_name
    _l_(1429)

except ImportError:
    pass

