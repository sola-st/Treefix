# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
r = Timestamp("2000-08-12T01:00:00").to_julian_date()
assert r == 2_451_768.5416666666666666
