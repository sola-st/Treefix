# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
idx = DatetimeIndex([Timestamp("2013-1-1", tz=tzstr), pd.NaT])

assert isna(idx[1])
assert idx[0].tzinfo is not None
