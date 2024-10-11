# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
# GH 23542
holidays = ["2018-11-09"]
bh = CustomBusinessHour(
    start="08:00", end="17:00", weekmask=weekmask, holidays=holidays
)
result = Timestamp("2018-11-08 08:00") + mult * bh
expected = Timestamp(expected_time)
assert result == expected
