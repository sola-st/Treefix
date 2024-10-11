# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# see gh-1511
name = "x"

ser = Series([0, -1, 0, 1, -3], name=name)
ind = cut(ser, [0, 1], labels=False)

exp = Series([np.nan, np.nan, np.nan, 0, np.nan], name=name)
tm.assert_series_equal(ind, exp)
