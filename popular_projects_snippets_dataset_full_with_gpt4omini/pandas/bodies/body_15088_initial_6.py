import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

index_or_series = pd.Series(np.array([1, 2, 3])) # pragma: no cover
arr = np.array([1, 2, 3]) # pragma: no cover
attr = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
from l3.Runtime import _l_
box = index_or_series
_l_(9667)

result = box(arr, copy=False).array
_l_(9668)

if attr:
    _l_(9671)

    arr = getattr(arr, attr)
    _l_(9669)
    result = getattr(result, attr)
    _l_(9670)

assert result is arr
_l_(9672)
