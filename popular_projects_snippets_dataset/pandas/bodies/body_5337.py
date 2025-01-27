# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# frequency conversion tests: from Weekly Frequency
ival_W = Period(freq="W", year=2007, month=1, day=1)

ival_WSUN = Period(freq="W", year=2007, month=1, day=7)
ival_WSAT = Period(freq="W-SAT", year=2007, month=1, day=6)
ival_WFRI = Period(freq="W-FRI", year=2007, month=1, day=5)
ival_WTHU = Period(freq="W-THU", year=2007, month=1, day=4)
ival_WWED = Period(freq="W-WED", year=2007, month=1, day=3)
ival_WTUE = Period(freq="W-TUE", year=2007, month=1, day=2)
ival_WMON = Period(freq="W-MON", year=2007, month=1, day=1)

ival_WSUN_to_D_start = Period(freq="D", year=2007, month=1, day=1)
ival_WSUN_to_D_end = Period(freq="D", year=2007, month=1, day=7)
ival_WSAT_to_D_start = Period(freq="D", year=2006, month=12, day=31)
ival_WSAT_to_D_end = Period(freq="D", year=2007, month=1, day=6)
ival_WFRI_to_D_start = Period(freq="D", year=2006, month=12, day=30)
ival_WFRI_to_D_end = Period(freq="D", year=2007, month=1, day=5)
ival_WTHU_to_D_start = Period(freq="D", year=2006, month=12, day=29)
ival_WTHU_to_D_end = Period(freq="D", year=2007, month=1, day=4)
ival_WWED_to_D_start = Period(freq="D", year=2006, month=12, day=28)
ival_WWED_to_D_end = Period(freq="D", year=2007, month=1, day=3)
ival_WTUE_to_D_start = Period(freq="D", year=2006, month=12, day=27)
ival_WTUE_to_D_end = Period(freq="D", year=2007, month=1, day=2)
ival_WMON_to_D_start = Period(freq="D", year=2006, month=12, day=26)
ival_WMON_to_D_end = Period(freq="D", year=2007, month=1, day=1)

ival_W_end_of_year = Period(freq="W", year=2007, month=12, day=31)
ival_W_end_of_quarter = Period(freq="W", year=2007, month=3, day=31)
ival_W_end_of_month = Period(freq="W", year=2007, month=1, day=31)
ival_W_to_A = Period(freq="A", year=2007)
ival_W_to_Q = Period(freq="Q", year=2007, quarter=1)
ival_W_to_M = Period(freq="M", year=2007, month=1)

if Period(freq="D", year=2007, month=12, day=31).weekday == 6:
    ival_W_to_A_end_of_year = Period(freq="A", year=2007)
else:
    ival_W_to_A_end_of_year = Period(freq="A", year=2008)

if Period(freq="D", year=2007, month=3, day=31).weekday == 6:
    ival_W_to_Q_end_of_quarter = Period(freq="Q", year=2007, quarter=1)
else:
    ival_W_to_Q_end_of_quarter = Period(freq="Q", year=2007, quarter=2)

if Period(freq="D", year=2007, month=1, day=31).weekday == 6:
    ival_W_to_M_end_of_month = Period(freq="M", year=2007, month=1)
else:
    ival_W_to_M_end_of_month = Period(freq="M", year=2007, month=2)

ival_W_to_B_start = Period(freq="B", year=2007, month=1, day=1)
ival_W_to_B_end = Period(freq="B", year=2007, month=1, day=5)
ival_W_to_D_start = Period(freq="D", year=2007, month=1, day=1)
ival_W_to_D_end = Period(freq="D", year=2007, month=1, day=7)
ival_W_to_H_start = Period(freq="H", year=2007, month=1, day=1, hour=0)
ival_W_to_H_end = Period(freq="H", year=2007, month=1, day=7, hour=23)
ival_W_to_T_start = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=0
)
ival_W_to_T_end = Period(
    freq="Min", year=2007, month=1, day=7, hour=23, minute=59
)
ival_W_to_S_start = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=0, second=0
)
ival_W_to_S_end = Period(
    freq="S", year=2007, month=1, day=7, hour=23, minute=59, second=59
)

assert ival_W.asfreq("A") == ival_W_to_A
assert ival_W_end_of_year.asfreq("A") == ival_W_to_A_end_of_year

assert ival_W.asfreq("Q") == ival_W_to_Q
assert ival_W_end_of_quarter.asfreq("Q") == ival_W_to_Q_end_of_quarter

assert ival_W.asfreq("M") == ival_W_to_M
assert ival_W_end_of_month.asfreq("M") == ival_W_to_M_end_of_month

assert ival_W.asfreq("B", "S") == ival_W_to_B_start
assert ival_W.asfreq("B", "E") == ival_W_to_B_end

assert ival_W.asfreq("D", "S") == ival_W_to_D_start
assert ival_W.asfreq("D", "E") == ival_W_to_D_end

assert ival_WSUN.asfreq("D", "S") == ival_WSUN_to_D_start
assert ival_WSUN.asfreq("D", "E") == ival_WSUN_to_D_end
assert ival_WSAT.asfreq("D", "S") == ival_WSAT_to_D_start
assert ival_WSAT.asfreq("D", "E") == ival_WSAT_to_D_end
assert ival_WFRI.asfreq("D", "S") == ival_WFRI_to_D_start
assert ival_WFRI.asfreq("D", "E") == ival_WFRI_to_D_end
assert ival_WTHU.asfreq("D", "S") == ival_WTHU_to_D_start
assert ival_WTHU.asfreq("D", "E") == ival_WTHU_to_D_end
assert ival_WWED.asfreq("D", "S") == ival_WWED_to_D_start
assert ival_WWED.asfreq("D", "E") == ival_WWED_to_D_end
assert ival_WTUE.asfreq("D", "S") == ival_WTUE_to_D_start
assert ival_WTUE.asfreq("D", "E") == ival_WTUE_to_D_end
assert ival_WMON.asfreq("D", "S") == ival_WMON_to_D_start
assert ival_WMON.asfreq("D", "E") == ival_WMON_to_D_end

assert ival_W.asfreq("H", "S") == ival_W_to_H_start
assert ival_W.asfreq("H", "E") == ival_W_to_H_end
assert ival_W.asfreq("Min", "S") == ival_W_to_T_start
assert ival_W.asfreq("Min", "E") == ival_W_to_T_end
assert ival_W.asfreq("S", "S") == ival_W_to_S_start
assert ival_W.asfreq("S", "E") == ival_W_to_S_end

assert ival_W.asfreq("W") == ival_W

msg = INVALID_FREQ_ERR_MSG
with pytest.raises(ValueError, match=msg):
    ival_W.asfreq("WK")
