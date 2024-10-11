# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_mask.py
# see gh-21891
ser = Series([1, 2])
res = ser.mask([True, False])

exp = Series([np.nan, 2])
tm.assert_series_equal(res, exp)
