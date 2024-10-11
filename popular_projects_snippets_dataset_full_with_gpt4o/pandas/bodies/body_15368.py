# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#20441
arr = date_range("2017", periods=4, tz="US/Eastern")
index = [(0, 1), (0, 2), (0, 3), (0, 4)]
result = Series(arr, index=index)
expected = result.copy()
result[(0, 1)] = np.nan
expected.iloc[0] = np.nan
tm.assert_series_equal(result, expected)
