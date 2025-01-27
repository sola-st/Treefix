# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# GH #21877
expected = Timedelta(1, unit="s")
assert to_timedelta("P0DT0H0M1S") == expected
