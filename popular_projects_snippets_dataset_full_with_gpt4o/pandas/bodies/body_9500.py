# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_construction.py
# to_numpy can be zero-copy if no missing values
arr = pd.array([True, False, True], dtype="boolean")
result = arr.to_numpy(dtype=bool)
result[0] = False
tm.assert_extension_array_equal(
    arr, pd.array([False, False, True], dtype="boolean")
)

arr = pd.array([True, False, True], dtype="boolean")
result = arr.to_numpy(dtype=bool, copy=True)
result[0] = False
tm.assert_extension_array_equal(arr, pd.array([True, False, True], dtype="boolean"))
