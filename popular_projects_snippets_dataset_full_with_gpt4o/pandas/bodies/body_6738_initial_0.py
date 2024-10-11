import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover
from pandas.api.types import IntervalDtype # pragma: no cover
from pandas.testing import assert_index_equal # pragma: no cover

IntervalIndex = pd.IntervalIndex # pragma: no cover
subtype_start = 'int64' # pragma: no cover
subtype_end = 'float64' # pragma: no cover
tm = type('Mock', (object,), {'assert_index_equal': assert_index_equal}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
from l3.Runtime import _l_
index = IntervalIndex.from_breaks(np.arange(100, dtype=subtype_start))
_l_(16046)
dtype = IntervalDtype(subtype_end, index.closed)
_l_(16047)
result = index.astype(dtype)
_l_(16048)
expected = IntervalIndex.from_arrays(
    index.left.astype(subtype_end),
    index.right.astype(subtype_end),
    closed=index.closed,
)
_l_(16049)
tm.assert_index_equal(result, expected)
_l_(16050)
