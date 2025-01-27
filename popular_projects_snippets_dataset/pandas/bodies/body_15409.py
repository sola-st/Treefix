# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# ensure that one can set something to np.nan
ser = Series(Categorical([1, 2, 3]))
exp = Series(Categorical([1, np.nan, 3], categories=[1, 2, 3]))
ser[1] = np.nan
tm.assert_series_equal(ser, exp)
