# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
assert BDay().freqstr == "B"
assert BDay(2).freqstr == "2B"
assert BMonthEnd().freqstr == "BM"
assert Week(weekday=0).freqstr == "W-MON"
assert Week(weekday=1).freqstr == "W-TUE"
assert Week(weekday=2).freqstr == "W-WED"
assert Week(weekday=3).freqstr == "W-THU"
assert Week(weekday=4).freqstr == "W-FRI"

assert LastWeekOfMonth(weekday=WeekDay.SUN).freqstr == "LWOM-SUN"
