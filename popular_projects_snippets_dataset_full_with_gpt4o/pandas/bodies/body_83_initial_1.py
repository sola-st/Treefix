import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

Series = pd.Series # pragma: no cover
def isna(obj): return pd.isna(obj) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
from l3.Runtime import _l_
left = Series({"a": 1.0, "b": 2.0, "c": 3.0, "d": 4})
_l_(21942)
right = Series({1: 11, 2: 22, 3: 33})
_l_(21943)

assert left.dtype == np.float_
_l_(21944)
assert issubclass(right.dtype.type, np.integer)
_l_(21945)

merged = left.map(right)
_l_(21946)
assert merged.dtype == np.float_
_l_(21947)
assert isna(merged["d"])
_l_(21948)
assert not isna(merged["c"])
_l_(21949)
