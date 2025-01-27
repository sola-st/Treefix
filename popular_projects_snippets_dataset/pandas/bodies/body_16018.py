# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_is_monotonic.py

ser = Series(date_range("20130101", periods=10))
assert ser.is_monotonic_increasing is True
assert ser.is_monotonic_increasing is True

ser = Series(list(reversed(ser)))
assert ser.is_monotonic_increasing is False
assert ser.is_monotonic_decreasing is True
