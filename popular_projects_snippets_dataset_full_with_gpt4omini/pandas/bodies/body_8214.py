# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
dt = dateutil.parser.parse("2012-06-13T01:39:00Z")
dt = dt.replace(tzinfo=tzlocal())

arr = np.array([dt], dtype=object)

result = to_datetime(arr, utc=True)
assert result.tz is timezone.utc

rng = date_range("2012-11-03 03:00", "2012-11-05 03:00", tz=tzlocal())
arr = rng.to_pydatetime()
result = to_datetime(arr, utc=True)
assert result.tz is timezone.utc
