# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_asfreq.py
# frequency conversion tests: from Annual Frequency

ival_A = Period(freq="A", year=2007)

ival_AJAN = Period(freq="A-JAN", year=2007)
ival_AJUN = Period(freq="A-JUN", year=2007)
ival_ANOV = Period(freq="A-NOV", year=2007)

ival_A_to_Q_start = Period(freq="Q", year=2007, quarter=1)
ival_A_to_Q_end = Period(freq="Q", year=2007, quarter=4)
ival_A_to_M_start = Period(freq="M", year=2007, month=1)
ival_A_to_M_end = Period(freq="M", year=2007, month=12)
ival_A_to_W_start = Period(freq="W", year=2007, month=1, day=1)
ival_A_to_W_end = Period(freq="W", year=2007, month=12, day=31)
ival_A_to_B_start = Period(freq="B", year=2007, month=1, day=1)
ival_A_to_B_end = Period(freq="B", year=2007, month=12, day=31)
ival_A_to_D_start = Period(freq="D", year=2007, month=1, day=1)
ival_A_to_D_end = Period(freq="D", year=2007, month=12, day=31)
ival_A_to_H_start = Period(freq="H", year=2007, month=1, day=1, hour=0)
ival_A_to_H_end = Period(freq="H", year=2007, month=12, day=31, hour=23)
ival_A_to_T_start = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=0
)
ival_A_to_T_end = Period(
    freq="Min", year=2007, month=12, day=31, hour=23, minute=59
)
ival_A_to_S_start = Period(
    freq="S", year=2007, month=1, day=1, hour=0, minute=0, second=0
)
ival_A_to_S_end = Period(
    freq="S", year=2007, month=12, day=31, hour=23, minute=59, second=59
)

ival_AJAN_to_D_end = Period(freq="D", year=2007, month=1, day=31)
ival_AJAN_to_D_start = Period(freq="D", year=2006, month=2, day=1)
ival_AJUN_to_D_end = Period(freq="D", year=2007, month=6, day=30)
ival_AJUN_to_D_start = Period(freq="D", year=2006, month=7, day=1)
ival_ANOV_to_D_end = Period(freq="D", year=2007, month=11, day=30)
ival_ANOV_to_D_start = Period(freq="D", year=2006, month=12, day=1)

assert ival_A.asfreq("Q", "S") == ival_A_to_Q_start
assert ival_A.asfreq("Q", "e") == ival_A_to_Q_end
assert ival_A.asfreq("M", "s") == ival_A_to_M_start
assert ival_A.asfreq("M", "E") == ival_A_to_M_end
assert ival_A.asfreq("W", "S") == ival_A_to_W_start
assert ival_A.asfreq("W", "E") == ival_A_to_W_end
assert ival_A.asfreq("B", "S") == ival_A_to_B_start
assert ival_A.asfreq("B", "E") == ival_A_to_B_end
assert ival_A.asfreq("D", "S") == ival_A_to_D_start
assert ival_A.asfreq("D", "E") == ival_A_to_D_end
assert ival_A.asfreq("H", "S") == ival_A_to_H_start
assert ival_A.asfreq("H", "E") == ival_A_to_H_end
assert ival_A.asfreq("min", "S") == ival_A_to_T_start
assert ival_A.asfreq("min", "E") == ival_A_to_T_end
assert ival_A.asfreq("T", "S") == ival_A_to_T_start
assert ival_A.asfreq("T", "E") == ival_A_to_T_end
assert ival_A.asfreq("S", "S") == ival_A_to_S_start
assert ival_A.asfreq("S", "E") == ival_A_to_S_end

assert ival_AJAN.asfreq("D", "S") == ival_AJAN_to_D_start
assert ival_AJAN.asfreq("D", "E") == ival_AJAN_to_D_end

assert ival_AJUN.asfreq("D", "S") == ival_AJUN_to_D_start
assert ival_AJUN.asfreq("D", "E") == ival_AJUN_to_D_end

assert ival_ANOV.asfreq("D", "S") == ival_ANOV_to_D_start
assert ival_ANOV.asfreq("D", "E") == ival_ANOV_to_D_end

assert ival_A.asfreq("A") == ival_A
