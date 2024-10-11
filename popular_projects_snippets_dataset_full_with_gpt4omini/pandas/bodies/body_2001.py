# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-13352
result = to_numeric(data, **kwargs)
expected = np.array([1, 2, 3], dtype=exp_dtype)
tm.assert_numpy_array_equal(result, expected)
