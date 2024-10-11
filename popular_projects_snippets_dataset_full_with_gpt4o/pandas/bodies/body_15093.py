# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
obj = index_or_series(values)
result = obj.to_numpy(dtype=dtype, na_value=na_value)
expected = np.array(expected)
tm.assert_numpy_array_equal(result, expected)
