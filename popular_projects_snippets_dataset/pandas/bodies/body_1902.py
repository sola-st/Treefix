# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# see gh-5430
local_timezone = "dateutil/America/Los_Angeles"

start = datetime(
    year=2013, month=11, day=1, hour=0, minute=0, tzinfo=dateutil.tz.tzutc()
)
# 1 day later
end = datetime(
    year=2013, month=11, day=2, hour=0, minute=0, tzinfo=dateutil.tz.tzutc()
)

index = date_range(start, end, freq="H", name="idx")

series = Series(1, index=index)
series = series.tz_convert(local_timezone)
result = series.resample("D", kind="period").mean()

# Create the expected series
# Index is moved back a day with the timezone conversion from UTC to
# Pacific
expected_index = (
    period_range(start=start, end=end, freq="D", name="idx") - offsets.Day()
)
expected = Series(1.0, index=expected_index)
tm.assert_series_equal(result, expected)
