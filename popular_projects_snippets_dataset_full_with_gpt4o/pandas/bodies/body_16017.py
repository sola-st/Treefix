# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_is_monotonic.py

ser = Series(np.random.randint(0, 10, size=1000))
assert not ser.is_monotonic_increasing
ser = Series(np.arange(1000))
assert ser.is_monotonic_increasing is True
assert ser.is_monotonic_increasing is True
ser = Series(np.arange(1000, 0, -1))
assert ser.is_monotonic_decreasing is True
