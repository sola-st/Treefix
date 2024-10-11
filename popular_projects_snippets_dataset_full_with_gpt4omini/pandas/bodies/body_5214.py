# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
assert td.min <= td
assert td.min._creso == td._creso
assert td.min.value == NaT.value + 1
