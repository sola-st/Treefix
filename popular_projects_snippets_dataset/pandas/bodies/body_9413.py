# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py
a = pd.array([1, 2, 3, None, 5], dtype=dtype)
b = pd.array([0, 1, None, 3, 4], dtype=dtype)

result = a % b
expected = pd.array([0, 0, None, None, 1], dtype=dtype)
tm.assert_extension_array_equal(result, expected)
