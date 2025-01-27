# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# frequency conversion tests: from Business Frequency"

ival_D = Period(freq="D", year=2007, month=1, day=1)
ival_D_end_of_year = Period(freq="D", year=2007, month=12, day=31)
ival_D_end_of_quarter = Period(freq="D", year=2007, month=3, day=31)
ival_D_end_of_month = Period(freq="D", year=2007, month=1, day=31)
ival_D_end_of_week = Period(freq="D", year=2007, month=1, day=7)

ival_D_friday = Period(freq="D", year=2007, month=1, day=5)
ival_D_saturday = Period(freq="D", year=2007, month=1, day=6)
ival_D_sunday = Period(freq="D", year=2007, month=1, day=7)

ival_B_friday = Period(freq="B", year=2007, month=1, day=5)
ival_B_monday = Period(freq="B", year=2007, month=1, day=8)

ival_D_to_A = Period(freq="A", year=2007)

ival_Deoq_to_AJAN = Period(freq="A-JAN", year=2008)
ival_Deoq_to_AJUN = Period(freq="A-JUN", year=2007)
ival_Deoq_to_ADEC = Period(freq="A-DEC", year=2007)

ival_D_to_QEJAN = Period(freq="Q-JAN", year=2007, quarter=4)
ival_D_to_QEJUN = Period(freq="Q-JUN", year=2007, quarter=3)
ival_D_to_QEDEC = Period(freq="Q-DEC", year=2007, quarter=1)

ival_D_to_M = Period(freq="M", year=2007, month=1)
ival_D_to_W = Period(freq="W", year=2007, month=1, day=7)

ival_D_to_H_start = Period(freq="H", year=2007, month=1, day=1, hour=0)
ival_D_to_H_end = Period(freq="H", year=2007, month=1, day=1, hour=23)
ival_D_to_T_start = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=0
)
ival_D_to_T_end = Period(
    freq="Min", year=2007, month=1, day=1, hour=23, minute=59
)
ival_D_to_S_start = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=0, second=0
)
ival_D_to_S_end = Period(
    freq="S", year=2007, month=1, day=1, hour=23, minute=59, second=59
)

assert ival_D.asfreq("A") == ival_D_to_A

assert ival_D_end_of_quarter.asfreq("A-JAN") == ival_Deoq_to_AJAN
assert ival_D_end_of_quarter.asfreq("A-JUN") == ival_Deoq_to_AJUN
assert ival_D_end_of_quarter.asfreq("A-DEC") == ival_Deoq_to_ADEC

assert ival_D_end_of_year.asfreq("A") == ival_D_to_A
assert ival_D_end_of_quarter.asfreq("Q") == ival_D_to_QEDEC
assert ival_D.asfreq("Q-JAN") == ival_D_to_QEJAN
assert ival_D.asfreq("Q-JUN") == ival_D_to_QEJUN
assert ival_D.asfreq("Q-DEC") == ival_D_to_QEDEC
assert ival_D.asfreq("M") == ival_D_to_M
assert ival_D_end_of_month.asfreq("M") == ival_D_to_M
assert ival_D.asfreq("W") == ival_D_to_W
assert ival_D_end_of_week.asfreq("W") == ival_D_to_W

assert ival_D_friday.asfreq("B") == ival_B_friday
assert ival_D_saturday.asfreq("B", "S") == ival_B_friday
assert ival_D_saturday.asfreq("B", "E") == ival_B_monday
assert ival_D_sunday.asfreq("B", "S") == ival_B_friday
assert ival_D_sunday.asfreq("B", "E") == ival_B_monday

assert ival_D.asfreq("H", "S") == ival_D_to_H_start
assert ival_D.asfreq("H", "E") == ival_D_to_H_end
assert ival_D.asfreq("Min", "S") == ival_D_to_T_start
assert ival_D.asfreq("Min", "E") == ival_D_to_T_end
assert ival_D.asfreq("S", "S") == ival_D_to_S_start
assert ival_D.asfreq("S", "E") == ival_D_to_S_end

assert ival_D.asfreq("D") == ival_D
