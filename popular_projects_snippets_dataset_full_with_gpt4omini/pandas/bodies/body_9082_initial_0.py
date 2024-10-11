SparseDtype = type('SparseDtype', (object,), {'__init__': lambda self, dtype, fill_value=None: setattr(self, 'dtype', dtype) or setattr(self, 'fill_value', fill_value), '__eq__': lambda self, other: isinstance(other, SparseDtype) and self.dtype == other.dtype and self.fill_value == other.fill_value}) # pragma: no cover

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
