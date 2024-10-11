# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 12902
a = Series(data=np.arange(4) * (1 + 2j), index=[0, 0, 1, 1])
expected = Series((1 + 2j, 5 + 10j))

result = a.groupby(level=0).sum()
tm.assert_series_equal(result, expected)
