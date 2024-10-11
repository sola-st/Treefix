# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
expected = Timedelta._from_value_and_reso(1, ts._creso)
result = ts.resolution
assert result == expected
assert result._creso == expected._creso
