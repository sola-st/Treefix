# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
msg = "time data must be specified only with hour and minute"
with pytest.raises(ValueError, match=msg):
    CustomBusinessHour(start=dt_time(11, 0, 5))
msg = "time data must match '%H:%M' format"
with pytest.raises(ValueError, match=msg):
    CustomBusinessHour(start="AAA")
msg = "time data must match '%H:%M' format"
with pytest.raises(ValueError, match=msg):
    CustomBusinessHour(start="14:00:05")
