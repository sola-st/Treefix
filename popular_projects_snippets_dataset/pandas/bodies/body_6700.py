# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_range.py
# not enough params
msg = (
    "Of the four parameters: start, end, periods, and freq, "
    "exactly three must be specified"
)

with pytest.raises(ValueError, match=msg):
    interval_range(start=0)

with pytest.raises(ValueError, match=msg):
    interval_range(end=5)

with pytest.raises(ValueError, match=msg):
    interval_range(periods=2)

with pytest.raises(ValueError, match=msg):
    interval_range()

# too many params
with pytest.raises(ValueError, match=msg):
    interval_range(start=0, end=5, periods=6, freq=1.5)

# mixed units
msg = "start, end, freq need to be type compatible"
with pytest.raises(TypeError, match=msg):
    interval_range(start=0, end=Timestamp("20130101"), freq=2)

with pytest.raises(TypeError, match=msg):
    interval_range(start=0, end=Timedelta("1 day"), freq=2)

with pytest.raises(TypeError, match=msg):
    interval_range(start=0, end=10, freq="D")

with pytest.raises(TypeError, match=msg):
    interval_range(start=Timestamp("20130101"), end=10, freq="D")

with pytest.raises(TypeError, match=msg):
    interval_range(
        start=Timestamp("20130101"), end=Timedelta("1 day"), freq="D"
    )

with pytest.raises(TypeError, match=msg):
    interval_range(
        start=Timestamp("20130101"), end=Timestamp("20130110"), freq=2
    )

with pytest.raises(TypeError, match=msg):
    interval_range(start=Timedelta("1 day"), end=10, freq="D")

with pytest.raises(TypeError, match=msg):
    interval_range(
        start=Timedelta("1 day"), end=Timestamp("20130110"), freq="D"
    )

with pytest.raises(TypeError, match=msg):
    interval_range(start=Timedelta("1 day"), end=Timedelta("10 days"), freq=2)

# invalid periods
msg = "periods must be a number, got foo"
with pytest.raises(TypeError, match=msg):
    interval_range(start=0, periods="foo")

# invalid start
msg = "start must be numeric or datetime-like, got foo"
with pytest.raises(ValueError, match=msg):
    interval_range(start="foo", periods=10)

# invalid end
msg = r"end must be numeric or datetime-like, got \(0, 1\]"
with pytest.raises(ValueError, match=msg):
    interval_range(end=Interval(0, 1), periods=10)

# invalid freq for datetime-like
msg = "freq must be numeric or convertible to DateOffset, got foo"
with pytest.raises(ValueError, match=msg):
    interval_range(start=0, end=10, freq="foo")

with pytest.raises(ValueError, match=msg):
    interval_range(start=Timestamp("20130101"), periods=10, freq="foo")

with pytest.raises(ValueError, match=msg):
    interval_range(end=Timedelta("1 day"), periods=10, freq="foo")

# mixed tz
start = Timestamp("2017-01-01", tz="US/Eastern")
end = Timestamp("2017-01-07", tz="US/Pacific")
msg = "Start and end cannot both be tz-aware with different timezones"
with pytest.raises(TypeError, match=msg):
    interval_range(start=start, end=end)
