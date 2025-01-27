# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
utc_range = date_range("1/1/2000", periods=20, tz="UTC")
eastern_range = utc_range.tz_convert("US/Eastern")
berlin_range = utc_range.tz_convert("Europe/Berlin")

for a, b, c in zip(utc_range, eastern_range, berlin_range):
    assert a == b
    assert b == c
    assert a == c

assert (utc_range == eastern_range).all()
assert (utc_range == berlin_range).all()
assert (berlin_range == eastern_range).all()
