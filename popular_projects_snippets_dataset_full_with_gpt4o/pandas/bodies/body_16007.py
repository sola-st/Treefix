# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_isin.py
# https://github.com/pandas-dev/pandas/issues/37174
arr = np.array([1, 2, 3])
arr.setflags(write=False)
s = Series([1, 2, 3])
result = s.isin(arr)
expected = Series([True, True, True])
tm.assert_series_equal(result, expected)
