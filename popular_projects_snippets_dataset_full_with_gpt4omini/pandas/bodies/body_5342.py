# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# frequency conversion tests: from Minutely Frequency"

ival_T = Period(freq="Min", year=2007, month=1, day=1, hour=0, minute=0)
ival_T_end_of_year = Period(
    freq="Min", year=2007, month=12, day=31, hour=23, minute=59
)
ival_T_end_of_quarter = Period(
    freq="Min", year=2007, month=3, day=31, hour=23, minute=59
)
ival_T_end_of_month = Period(
    freq="Min", year=2007, month=1, day=31, hour=23, minute=59
)
ival_T_end_of_week = Period(
    freq="Min", year=2007, month=1, day=7, hour=23, minute=59
)
ival_T_end_of_day = Period(
    freq="Min", year=2007, month=1, day=1, hour=23, minute=59
)
ival_T_end_of_bus = Period(
    freq="Min", year=2007, month=1, day=1, hour=23, minute=59
)
ival_T_end_of_hour = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=59
)

ival_T_to_A = Period(freq="A", year=2007)
ival_T_to_Q = Period(freq="Q", year=2007, quarter=1)
ival_T_to_M = Period(freq="M", year=2007, month=1)
ival_T_to_W = Period(freq="W", year=2007, month=1, day=7)
ival_T_to_D = Period(freq="D", year=2007, month=1, day=1)
ival_T_to_B = Period(freq="B", year=2007, month=1, day=1)
ival_T_to_H = Period(freq="H", year=2007, month=1, day=1, hour=0)

ival_T_to_S_start = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=0, second=0
)
ival_T_to_S_end = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=0, second=59
)

assert ival_T.asfreq("A") == ival_T_to_A
assert ival_T_end_of_year.asfreq("A") == ival_T_to_A
assert ival_T.asfreq("Q") == ival_T_to_Q
assert ival_T_end_of_quarter.asfreq("Q") == ival_T_to_Q
assert ival_T.asfreq("M") == ival_T_to_M
assert ival_T_end_of_month.asfreq("M") == ival_T_to_M
assert ival_T.asfreq("W") == ival_T_to_W
assert ival_T_end_of_week.asfreq("W") == ival_T_to_W
assert ival_T.asfreq("D") == ival_T_to_D
assert ival_T_end_of_day.asfreq("D") == ival_T_to_D
assert ival_T.asfreq("B") == ival_T_to_B
assert ival_T_end_of_bus.asfreq("B") == ival_T_to_B
assert ival_T.asfreq("H") == ival_T_to_H
assert ival_T_end_of_hour.asfreq("H") == ival_T_to_H

assert ival_T.asfreq("S", "S") == ival_T_to_S_start
assert ival_T.asfreq("S", "E") == ival_T_to_S_end

assert ival_T.asfreq("Min") == ival_T
