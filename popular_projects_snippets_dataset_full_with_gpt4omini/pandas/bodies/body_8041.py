# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
from l3.Runtime import _l_
index = Index(vals, name=dtype)
_l_(5699)
result = index._simple_new(index.values, dtype)
_l_(5700)
tm.assert_index_equal(result, index)
_l_(5701)
