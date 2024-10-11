# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 23579
kwargs = {"year": 2018, "month": 1, "day": 1, "tzinfo": pytz.utc}
msg = "Cannot pass a datetime or Timestamp"
with pytest.raises(ValueError, match=msg):
    Timestamp(box(**kwargs), tz="US/Pacific")
msg = "Cannot pass a datetime or Timestamp"
with pytest.raises(ValueError, match=msg):
    Timestamp(box(**kwargs), tzinfo=pytz.timezone("US/Pacific"))
