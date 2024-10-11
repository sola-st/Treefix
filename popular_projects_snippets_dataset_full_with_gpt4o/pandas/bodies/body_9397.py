# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_dtypes.py
a = pd.array([1, 2], dtype="Int32")
result = a.astype("int64")
expected = np.array([1, 2], dtype="int64")
tm.assert_numpy_array_equal(result, expected)

a = pd.array([1, 2], dtype="UInt32")
result = a.astype("uint64")
expected = np.array([1, 2], dtype="uint64")
tm.assert_numpy_array_equal(result, expected)
