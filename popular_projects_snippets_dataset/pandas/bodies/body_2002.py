# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-13352
smallest_int_dtype = np.dtype(np.typecodes["Integer"][0])
expected = np.array([1, 2, 3], dtype=smallest_int_dtype)

res = to_numeric(data, downcast=signed_downcast)
tm.assert_numpy_array_equal(res, expected)
