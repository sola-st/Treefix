# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# frequency conversion tests: from Hourly Frequency"

ival_H = Period(freq="H", year=2007, month=1, day=1, hour=0)
ival_H_end_of_year = Period(freq="H", year=2007, month=12, day=31, hour=23)
ival_H_end_of_quarter = Period(freq="H", year=2007, month=3, day=31, hour=23)
ival_H_end_of_month = Period(freq="H", year=2007, month=1, day=31, hour=23)
ival_H_end_of_week = Period(freq="H", year=2007, month=1, day=7, hour=23)
ival_H_end_of_day = Period(freq="H", year=2007, month=1, day=1, hour=23)
ival_H_end_of_bus = Period(freq="H", year=2007, month=1, day=1, hour=23)

ival_H_to_A = Period(freq="A", year=2007)
ival_H_to_Q = Period(freq="Q", year=2007, quarter=1)
ival_H_to_M = Period(freq="M", year=2007, month=1)
ival_H_to_W = Period(freq="W", year=2007, month=1, day=7)
ival_H_to_D = Period(freq="D", year=2007, month=1, day=1)
ival_H_to_B = Period(freq="B", year=2007, month=1, day=1)

ival_H_to_T_start = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=0
)
ival_H_to_T_end = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=59
)
ival_H_to_S_start = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=0, second=0
)
ival_H_to_S_end = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=59, second=59
)

assert ival_H.asfreq("A") == ival_H_to_A
assert ival_H_end_of_year.asfreq("A") == ival_H_to_A
assert ival_H.asfreq("Q") == ival_H_to_Q
assert ival_H_end_of_quarter.asfreq("Q") == ival_H_to_Q
assert ival_H.asfreq("M") == ival_H_to_M
assert ival_H_end_of_month.asfreq("M") == ival_H_to_M
assert ival_H.asfreq("W") == ival_H_to_W
assert ival_H_end_of_week.asfreq("W") == ival_H_to_W
assert ival_H.asfreq("D") == ival_H_to_D
assert ival_H_end_of_day.asfreq("D") == ival_H_to_D
assert ival_H.asfreq("B") == ival_H_to_B
assert ival_H_end_of_bus.asfreq("B") == ival_H_to_B

assert ival_H.asfreq("Min", "S") == ival_H_to_T_start
assert ival_H.asfreq("Min", "E") == ival_H_to_T_end
assert ival_H.asfreq("S", "S") == ival_H_to_S_start
assert ival_H.asfreq("S", "E") == ival_H_to_S_end

assert ival_H.asfreq("H") == ival_H
