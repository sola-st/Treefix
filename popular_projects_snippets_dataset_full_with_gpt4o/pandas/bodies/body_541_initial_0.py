dtype = 'example_dtype' # pragma: no cover
registry = type('Mock', (object,), {'dtypes': ['example_dtype', 'another_dtype']})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
from l3.Runtime import _l_
assert dtype in registry.dtypes
_l_(20583)
