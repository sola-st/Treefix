# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# the smallest integer dtype need not be np.(u)int8
data = ["256", 257, 258]

expected = np.array([256, 257, 258], dtype=expected_dtype)
res = to_numeric(data, downcast=downcast)
tm.assert_numpy_array_equal(res, expected)
