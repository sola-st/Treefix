# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_to_numpy.py
# to_numpy can be zero-copy if no missing values
arr = pd.array([0.1, 0.2, 0.3], dtype="Float64")
result = arr.to_numpy(dtype="float64")
result[0] = 10
tm.assert_extension_array_equal(arr, pd.array([10, 0.2, 0.3], dtype="Float64"))

arr = pd.array([0.1, 0.2, 0.3], dtype="Float64")
result = arr.to_numpy(dtype="float64", copy=True)
result[0] = 10
tm.assert_extension_array_equal(arr, pd.array([0.1, 0.2, 0.3], dtype="Float64"))
