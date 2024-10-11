# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
# Just checking that the fixture is giving us what we asked for
td = Timedelta._from_value_and_reso(val, unit)
assert td.value == val
assert td._creso == unit
assert td.days == 106752
