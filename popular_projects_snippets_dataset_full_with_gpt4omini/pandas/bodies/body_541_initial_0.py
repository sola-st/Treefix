import types # pragma: no cover

dtype = 'float32' # pragma: no cover
registry = type('Mock', (object,), {'dtypes': ['float32', 'int32', 'string']})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
from l3.Runtime import _l_
assert dtype in registry.dtypes
_l_(9089)
