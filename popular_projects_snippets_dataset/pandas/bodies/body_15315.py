# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
tz = timezones.maybe_get_tz(tzstr)

index = date_range(
    start="2012-12-24 16:00", end="2012-12-24 18:00", freq="H", tz=tzstr
)
ts = Series(index=index, data=index.hour)
time_pandas = Timestamp("2012-12-24 17:00", tz=tzstr)

dt = datetime(2012, 12, 24, 17, 0)
time_datetime = conversion.localize_pydatetime(dt, tz)
assert ts[time_pandas] == ts[time_datetime]
