SparseDtype = type('SparseDtype', (object,), {'__init__': lambda self, dtype, fill_value=None: None, '__eq__': lambda self, other: isinstance(other, SparseDtype) and self.fill_value == other.fill_value, 'dtype': None, 'fill_value': 0}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
from l3.Runtime import _l_
dtype = SparseDtype("int", 1)
_l_(8961)
result = SparseDtype(dtype, fill_value=2)
_l_(8962)
expected = SparseDtype("int", 2)
_l_(8963)
assert result == expected
_l_(8964)
