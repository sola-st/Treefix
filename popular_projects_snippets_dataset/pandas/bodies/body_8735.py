# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
tdi = timedelta_index
arr = TimedeltaArray(tdi)

expected = tdi.to_pytimedelta()
result = arr.to_pytimedelta()

tm.assert_numpy_array_equal(result, expected)
