# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
r = Timestamp("2000-04-12").to_julian_date()
assert r == 2_451_646.5
