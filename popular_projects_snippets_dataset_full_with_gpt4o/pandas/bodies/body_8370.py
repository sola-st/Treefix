# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
rng = date_range("20090415", "20090519", tz="dateutil/US/Eastern")
stamp = rng[0]

ts = Timestamp("20090415", tz="dateutil/US/Eastern")
assert ts == stamp
