# Extracted from ./data/repos/pandas/pandas/tests/extension/decimal/test_decimal.py
a = to_decimal([1, 2, 3])
result = np.exp(a)
expected = to_decimal(np.exp(a._data))
tm.assert_extension_array_equal(result, expected)
