# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_dict.py
# GH#16122
result = Series(datetime_series.to_dict(mapping), name="ts")
expected = datetime_series.copy()
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)

from_method = Series(datetime_series.to_dict(collections.Counter))
from_constructor = Series(collections.Counter(datetime_series.items()))
tm.assert_series_equal(from_method, from_constructor)
