# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# gh-15869, GH#11220
result = DataFrame(arr).dtypes
expected = Series([np.dtype("datetime64[ns]")])
tm.assert_series_equal(result, expected)
