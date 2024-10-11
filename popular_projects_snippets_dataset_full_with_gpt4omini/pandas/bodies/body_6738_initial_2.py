import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas.api.extensions import register_extension_dtype # pragma: no cover
from pandas import IntervalIndex, IntervalDtype # pragma: no cover
import pandas._testing as tm # pragma: no cover

IntervalIndex = pd.IntervalIndex # pragma: no cover
subtype_start = 'int64' # pragma: no cover
IntervalDtype = pd.IntervalDtype # pragma: no cover
subtype_end = 'int64' # pragma: no cover
tm = pd.testing # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
from l3.Runtime import _l_
index = IntervalIndex.from_breaks(np.arange(100, dtype=subtype_start))
_l_(4847)
dtype = IntervalDtype(subtype_end, index.closed)
_l_(4848)
result = index.astype(dtype)
_l_(4849)
expected = IntervalIndex.from_arrays(
    index.left.astype(subtype_end),
    index.right.astype(subtype_end),
    closed=index.closed,
)
_l_(4850)
tm.assert_index_equal(result, expected)
_l_(4851)
