# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
r = Timestamp("1700-06-23").to_julian_date()
assert r == 2_342_145.5
