# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
from l3.Runtime import _l_
a = DataFrame({"a": [1, 2, 3]})
_l_(20865)
b = DataFrame({"b": [3, 4, 5]})
_l_(20866)

with pytest.raises(TypeError, match="Passing 'suffixes' as a"):
    _l_(20868)

    merge(a, b, left_index=True, right_index=True, suffixes=suffixes)
    _l_(20867)
