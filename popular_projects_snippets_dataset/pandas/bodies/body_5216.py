# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
expected = Timedelta._from_value_and_reso(1, td._creso)
result = td.resolution
assert result == expected
assert result._creso == expected._creso
