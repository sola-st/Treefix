# Extracted from ./data/repos/pandas/pandas/tests/base/test_unique.py
obj = index_or_series_obj
obj = np.repeat(obj, range(1, len(obj) + 1))
result = obj.unique()

# dict.fromkeys preserves the order
unique_values = list(dict.fromkeys(obj.values))
if isinstance(obj, pd.MultiIndex):
    expected = pd.MultiIndex.from_tuples(unique_values)
    expected.names = obj.names
    tm.assert_index_equal(result, expected, exact=True)
elif isinstance(obj, pd.Index):
    expected = pd.Index(unique_values, dtype=obj.dtype)
    if is_datetime64tz_dtype(obj.dtype):
        expected = expected.normalize()
    tm.assert_index_equal(result, expected, exact=True)
else:
    expected = np.array(unique_values)
    tm.assert_numpy_array_equal(result, expected)
