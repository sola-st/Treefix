# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_searchsorted.py
idx = TimedeltaIndex(["1 day", "2 days", "3 days"])
result = idx.searchsorted(listlike_box(idx))
expected = np.arange(len(idx), dtype=result.dtype)
tm.assert_numpy_array_equal(result, expected)

result = idx._data.searchsorted(listlike_box(idx))
tm.assert_numpy_array_equal(result, expected)
