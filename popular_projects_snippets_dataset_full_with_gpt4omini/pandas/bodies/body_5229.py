# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert Timedelta(0) == np.timedelta64(0, "ns")
assert Timedelta(10) == np.timedelta64(10, "ns")
assert Timedelta(10, unit="ns") == np.timedelta64(10, "ns")

assert Timedelta(10, unit="us") == np.timedelta64(10, "us")
assert Timedelta(10, unit="ms") == np.timedelta64(10, "ms")
assert Timedelta(10, unit="s") == np.timedelta64(10, "s")
assert Timedelta(10, unit="d") == np.timedelta64(10, "D")
