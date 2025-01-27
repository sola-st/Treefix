# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rank.py
method, _ = results
if "i" in dtype:
    s = ser.dropna()
else:
    s = ser.astype(dtype)

res = s.rank(ascending=False)
expected = (s.max() - s).rank()
tm.assert_series_equal(res, expected)

expected = (s.max() - s).rank(method=method)
res2 = s.rank(method=method, ascending=False)
tm.assert_series_equal(res2, expected)
