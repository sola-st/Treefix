import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

Series = pd.Series # pragma: no cover
sort_kind = 'quicksort' # pragma: no cover
tm = type('Mock', (object,), {'assert_series_equal': staticmethod(tm.assert_series_equal)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
# GH#14444 & GH#13589:  Add support for sort algo choosing
from l3.Runtime import _l_
series = Series(index=[3, 2, 1, 4, 3], dtype=object)
_l_(9382)
expected_series = Series(index=[1, 2, 3, 3, 4], dtype=object)
_l_(9383)

index_sorted_series = series.sort_index(kind=sort_kind)
_l_(9384)
tm.assert_series_equal(expected_series, index_sorted_series)
_l_(9385)
