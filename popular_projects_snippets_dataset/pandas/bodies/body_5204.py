# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
res = td - td
expected = Timedelta._from_value_and_reso(0, unit)
assert res == expected
assert res._creso == unit
