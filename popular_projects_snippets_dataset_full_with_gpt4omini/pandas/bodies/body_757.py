# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
result = isna([[False]])
exp = np.array([[False]])
tm.assert_numpy_array_equal(result, exp)

result = isna([[1], [2]])
exp = np.array([[False], [False]])
tm.assert_numpy_array_equal(result, exp)

# list of strings / unicode
result = isna(["foo", "bar"])
exp = np.array([False, False])
tm.assert_numpy_array_equal(result, exp)

result = isna(["foo", "bar"])
exp = np.array([False, False])
tm.assert_numpy_array_equal(result, exp)

# GH20675
result = isna([np.NaN, "world"])
exp = np.array([True, False])
tm.assert_numpy_array_equal(result, exp)
