# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH 13034
result = Series([True, False, True])
result[0] = np.nan
expected = Series([np.nan, False, True], dtype=object)
tm.assert_series_equal(result, expected)
