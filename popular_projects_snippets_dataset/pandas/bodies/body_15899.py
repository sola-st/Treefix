# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_values.py
# https://github.com/pandas-dev/pandas/issues/23995
result = Series(data).values
expected = np.array(data.astype(object))
tm.assert_numpy_array_equal(result, expected)
