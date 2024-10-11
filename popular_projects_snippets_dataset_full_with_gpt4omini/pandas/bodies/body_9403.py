# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
a = pd.array([0, 1], dtype="Int64")
if in_series:
    a = pd.Series(a)

result = a.to_numpy(dtype=dtype)
expected = np.array([0, 1], dtype=dtype)
tm.assert_numpy_array_equal(result, expected)
