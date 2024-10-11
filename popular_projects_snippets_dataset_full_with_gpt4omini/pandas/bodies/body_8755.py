# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# https://github.com/pandas-dev/pandas/issues/32762
if not as_index:
    values = values._data

result = values.searchsorted(klass(values))
expected = np.array([0, 1], dtype=result.dtype)

tm.assert_numpy_array_equal(result, expected)
