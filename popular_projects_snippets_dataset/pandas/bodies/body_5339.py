# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# frequency conversion tests: from Business Frequency"

ival_B = Period(freq="B", year=2007, month=1, day=1)
ival_B_end_of_year = Period(freq="B", year=2007, month=12, day=31)
ival_B_end_of_quarter = Period(freq="B", year=2007, month=3, day=30)
ival_B_end_of_month = Period(freq="B", year=2007, month=1, day=31)
ival_B_end_of_week = Period(freq="B", year=2007, month=1, day=5)

ival_B_to_A = Period(freq="A", year=2007)
ival_B_to_Q = Period(freq="Q", year=2007, quarter=1)
ival_B_to_M = Period(freq="M", year=2007, month=1)
ival_B_to_W = Period(freq="W", year=2007, month=1, day=7)
ival_B_to_D = Period(freq="D", year=2007, month=1, day=1)
ival_B_to_H_start = Period(freq="H", year=2007, month=1, day=1, hour=0)
ival_B_to_H_end = Period(freq="H", year=2007, month=1, day=1, hour=23)
ival_B_to_T_start = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=0
)
ival_B_to_T_end = Period(
    freq="Min", year=2007, month=1, day=1, hour=23, minute=59
)
ival_B_to_S_start = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=0, second=0
)
ival_B_to_S_end = Period(
    freq="S", year=2007, month=1, day=1, hour=23, minute=59, second=59
)

assert ival_B.asfreq("A") == ival_B_to_A
assert ival_B_end_of_year.asfreq("A") == ival_B_to_A
assert ival_B.asfreq("Q") == ival_B_to_Q
assert ival_B_end_of_quarter.asfreq("Q") == ival_B_to_Q
assert ival_B.asfreq("M") == ival_B_to_M
assert ival_B_end_of_month.asfreq("M") == ival_B_to_M
assert ival_B.asfreq("W") == ival_B_to_W
assert ival_B_end_of_week.asfreq("W") == ival_B_to_W

assert ival_B.asfreq("D") == ival_B_to_D

assert ival_B.asfreq("H", "S") == ival_B_to_H_start
assert ival_B.asfreq("H", "E") == ival_B_to_H_end
assert ival_B.asfreq("Min", "S") == ival_B_to_T_start
assert ival_B.asfreq("Min", "E") == ival_B_to_T_end
assert ival_B.asfreq("S", "S") == ival_B_to_S_start
assert ival_B.asfreq("S", "E") == ival_B_to_S_end

assert ival_B.asfreq("B") == ival_B
