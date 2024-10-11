# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# GH 17927
result = Series(array).isin([1j, 1 + 1j, 1 + 2j])
tm.assert_series_equal(result, expected)
