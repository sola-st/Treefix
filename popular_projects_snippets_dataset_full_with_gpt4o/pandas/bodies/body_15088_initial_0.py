import pandas as pd # pragma: no cover

index_or_series = pd.Series # pragma: no cover
arr = pd.array([1, 2, 3]) # pragma: no cover
attr = 'dtype' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
from l3.Runtime import _l_
box = index_or_series
_l_(20362)

result = box(arr, copy=False).array
_l_(20363)

if attr:
    _l_(20366)

    arr = getattr(arr, attr)
    _l_(20364)
    result = getattr(result, attr)
    _l_(20365)

assert result is arr
_l_(20367)
