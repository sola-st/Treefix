# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_to_numpy.py
con = pd.Series if box else pd.array

# default (with or without missing values) -> object dtype
arr = con([0.1, 0.2, 0.3], dtype="Float64")
result = arr.to_numpy()
expected = np.array([0.1, 0.2, 0.3], dtype="object")
tm.assert_numpy_array_equal(result, expected)

arr = con([0.1, 0.2, None], dtype="Float64")
result = arr.to_numpy()
expected = np.array([0.1, 0.2, pd.NA], dtype="object")
tm.assert_numpy_array_equal(result, expected)
