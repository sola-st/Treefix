# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
tdi = timedelta_index
arr = TimedeltaArray(tdi)

result = getattr(arr, propname)
expected = np.array(getattr(tdi, propname), dtype=result.dtype)

tm.assert_numpy_array_equal(result, expected)
