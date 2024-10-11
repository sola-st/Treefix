# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
arr = np.empty(shape=shape, dtype=object)
result = isna(arr)
expected = np.ones(shape=shape, dtype=bool)
tm.assert_numpy_array_equal(result, expected)
