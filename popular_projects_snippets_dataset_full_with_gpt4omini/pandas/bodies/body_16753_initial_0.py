import pandas as pd # pragma: no cover
import pytest # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
merge = pd.merge # pragma: no cover
suffixes = ('_left', '_right') # pragma: no cover
pytest.raises = type('Mock', (object,), {'raises': staticmethod(lambda *args: None)}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
from l3.Runtime import _l_
a = DataFrame({"a": [1, 2, 3]})
_l_(10119)
b = DataFrame({"b": [3, 4, 5]})
_l_(10120)

with pytest.raises(TypeError, match="Passing 'suffixes' as a"):
    _l_(10122)

    merge(a, b, left_index=True, right_index=True, suffixes=suffixes)
    _l_(10121)
