# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
for offset in [offset1, offset2]:
    assert offset == offset

assert CustomBusinessHour() != CustomBusinessHour(-1)
assert CustomBusinessHour(start="09:00") == CustomBusinessHour()
assert CustomBusinessHour(start="09:00") != CustomBusinessHour(start="09:01")
assert CustomBusinessHour(start="09:00", end="17:00") != CustomBusinessHour(
    start="17:00", end="09:01"
)

assert CustomBusinessHour(weekmask="Tue Wed Thu Fri") != CustomBusinessHour(
    weekmask="Mon Tue Wed Thu Fri"
)
assert CustomBusinessHour(holidays=["2014-06-27"]) != CustomBusinessHour(
    holidays=["2014-06-28"]
)
