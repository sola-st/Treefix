# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/35762
dtype = pd.SparseDtype("datetime64[ns]")
result = Series(values, dtype=dtype)
arr = pd.arrays.SparseArray(values, dtype=dtype)
expected = Series(arr)
tm.assert_series_equal(result, expected)
