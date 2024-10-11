# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
s = Series(ser).astype(dtype)
result = s.rank(method="first", pct=True)
expected = Series(exp).astype(result.dtype)
tm.assert_series_equal(result, expected)
