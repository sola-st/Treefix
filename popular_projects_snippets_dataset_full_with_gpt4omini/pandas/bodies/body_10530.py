# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_cython.py
dr = bdate_range("1/1/2000", periods=50)
ts = Series(["A", "B", "C", "D", "E"] * 10, index=dr)

grouped = ts.groupby(lambda x: x.month)
summed = grouped.sum()
expected = grouped.agg(np.sum)
tm.assert_series_equal(summed, expected)
