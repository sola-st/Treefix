# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
tdi = TimedeltaIndex(["1 Day", "3 Hours"])
arr = TimedeltaArray(tdi)
assert list(arr) == list(tdi)

# Check that Index.__new__ knows what to do with TimedeltaArray
tdi2 = pd.Index(arr)
assert isinstance(tdi2, TimedeltaIndex)
assert list(tdi2) == list(arr)
