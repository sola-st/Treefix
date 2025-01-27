# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
# GH#40638
arr = pd.array([pd.NA, 1], dtype="string")
result = arr.to_numpy(na_value=True, dtype=bool)
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)
