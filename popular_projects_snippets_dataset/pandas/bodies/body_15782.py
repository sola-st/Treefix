# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#4405
result = series.astype(dtype)
expected = series.map(str)
tm.assert_series_equal(result, expected)
