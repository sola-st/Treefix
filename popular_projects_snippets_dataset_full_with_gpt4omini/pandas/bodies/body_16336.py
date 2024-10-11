# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
d = {"a": 0.0, "b": 1.0, "c": 2.0}

result = Series(d)
expected = Series(d, index=sorted(d.keys()))
tm.assert_series_equal(result, expected)

result = Series(d, index=["b", "c", "d", "a"])
expected = Series([1, 2, np.nan, 0], index=["b", "c", "d", "a"])
tm.assert_series_equal(result, expected)

pidx = tm.makePeriodIndex(100)
d = {pidx[0]: 0, pidx[1]: 1}
result = Series(d, index=pidx)
expected = Series(np.nan, pidx, dtype=np.float64)
expected.iloc[0] = 0
expected.iloc[1] = 1
tm.assert_series_equal(result, expected)
