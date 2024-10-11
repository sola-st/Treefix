# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py

td = Timedelta(10, unit="d")
assert isinstance(td, Timedelta)
assert isinstance(td, timedelta)
