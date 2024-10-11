# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
result = to_numeric(data)
expected = np.array(data, **arr_kwargs)
tm.assert_numpy_array_equal(result, expected)
