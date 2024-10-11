# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
a = pd.array([0, 1, None], dtype="Int64")
if in_series:
    a = pd.Series(a)

result = a.to_numpy(dtype="float64", na_value=np.nan)
expected = np.array([0.0, 1.0, np.nan], dtype="float64")
tm.assert_numpy_array_equal(result, expected)

result = a.to_numpy(dtype="int64", na_value=-1)
expected = np.array([0, 1, -1], dtype="int64")
tm.assert_numpy_array_equal(result, expected)

result = a.to_numpy(dtype="bool", na_value=False)
expected = np.array([False, True, False], dtype="bool")
tm.assert_numpy_array_equal(result, expected)
