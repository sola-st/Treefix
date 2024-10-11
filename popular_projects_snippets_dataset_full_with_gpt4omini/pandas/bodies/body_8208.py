# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
left = date_range("1/1/2011", periods=100, freq="H", tz="utc")
right = date_range("1/1/2011", periods=100, freq="H", tz="US/Eastern")

assert not left.equals(right)
