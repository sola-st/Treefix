# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_index.py
# GH#14444 & GH#13589:  Add support for sort algo choosing
from l3.Runtime import _l_
series = Series(index=[3, 2, 1, 4, 3], dtype=object)
_l_(19679)
expected_series = Series(index=[1, 2, 3, 3, 4], dtype=object)
_l_(19680)

index_sorted_series = series.sort_index(kind=sort_kind)
_l_(19681)
tm.assert_series_equal(expected_series, index_sorted_series)
_l_(19682)
