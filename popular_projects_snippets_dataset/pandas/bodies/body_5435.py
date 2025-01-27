# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
r = Timestamp("2100-08-12").to_julian_date()
assert r == 2_488_292.5
