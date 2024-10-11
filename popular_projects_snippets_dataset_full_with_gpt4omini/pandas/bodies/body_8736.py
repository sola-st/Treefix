# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
tdi = timedelta_index
arr = TimedeltaArray(tdi)

expected = tdi.total_seconds()
result = arr.total_seconds()

tm.assert_numpy_array_equal(result, expected.values)
